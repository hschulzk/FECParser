import pypyodbc
import datetime
connection = pypyodbc.connect(
'Driver={SQL Server};'
'Server=redacted;'
'Database=redacted;'
'uid=redacted;'
'pwd=redacted'
)

count = 0

def getElectionType(PGI):
	SQLCommand = ("SELECT id " "FROM ElectionTypes " "WHERE transaction_PGI = ?") 
	Values = [PGI]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False

def getCommitteeId(CMTEID):
	SQLCommand = ("SELECT id " "FROM committees " "WHERE cmte_id = ?") 
	Values = [CMTEID]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False

def getEntity(ENTITYTYPE):
	SQLCommand = ("SELECT id " "FROM entityType " "WHERE Entity_Type = ?") 
	Values = [ENTITYTYPE]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False
def getState(state):
	SQLCommand = ("SELECT id " "FROM states " "WHERE state = ?") 
	Values = [state]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False

def getDonor(name, city, state, zipcode, employer, occupation):
	SQLCommand = ("SELECT id " 
		"FROM donors " 
		"WHERE name = ? and city = ? and state = ? and zipcode = ? and employer = ? and occupation = ?") 
	Values = [name, city, state, zipcode, employer, occupation]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False			

def getTransaction(CMTEID, donorId, amount, SUB_ID):
	SQLCommand = ("SELECT id " "FROM transactions " "WHERE CMTE_ID = ? and donor = ? and amount = ? and SUB_ID = ?")
	Values = [CMTEID, donorId, amount, SUB_ID]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False

cursor = connection.cursor()
fileName = raw_input('Enter File to Parse:')
with open('itcont.txt', 'r') as fhand:
	content = fhand.read()
	for line in content:
		count += 1
		line = line.strip()
		line = line.split('|')


		#committeeInfo
		CMTEID = line[0]
		#If committeeID is in database, return the ID. Else, insert it and return that id
		committeeId = getCommitteeId(CMTEID)
		if not committeeId:
			Values = [CMTEID]
			SQLCommand = ("INSERT INTO committees " "(cmte_id) " "VALUES (?)")
			cursor.execute(SQLCommand,Values)
			connection.commit()
			committeeId = getCommitteeId(CMTEID)
		CMTEID = committeeId

		#electionType
		PGI = line[3]
		#If electionType is in database, return the ID. Else, insert it and return that id	
		electionType = getElectionType(PGI)
		if not electionType:
			Values = [PGI]	
			SQLCommand = ("INSERT INTO ElectionTypes " "(transaction_PGI) " "VALUES (?)")
			cursor.execute(SQLCommand,Values)
			connection.commit()
			electionType = getElectionType(PGI)
		PGI = electionType

		#entityType	
		ENTITYTYPE = line[6]
		#get entity type same as above
		entityType = getEntity(ENTITYTYPE)
		if not entityType:
			Values = [ENTITYTYPE]
			SQLCommand = ("INSERT INTO entityType " "(Entity_Type) " "VALUES (?)")
			cursor.execute(SQLCommand,Values)
			connection.commit()
			entityType = getEntity(ENTITYTYPE)
		ENTITYTYPE = entityType	

		#state
		state = line[9]
		stateid = getState(state)
		if not stateid:
			Values = [state]
			SQLCommand = ("INSERT INTO states " "(state) " "VALUES (?)")
			cursor.execute(SQLCommand,Values)
			connection.commit()
			stateid = getState(state)
		state = stateid	

		#Donor information
		Name = line[7]
		city = line[8]
		zipcode = line[10]
		employer = line[11]
		occupation = line[12]
		donorId = getDonor(Name, city, state, zipcode, employer, occupation)
		if not donorId:
			Values = [Name, city, state, zipcode, employer, occupation]
			SQLCommand = ("INSERT INTO donors " "(name, city, state, zipcode, employer, occupation) "  "VALUES (?,?,?,?,?,?)")		
			cursor.execute(SQLCommand,Values)
			connection.commit()
			donorId = getDonor(Name, city, state, zipcode, employer, occupation)	

		#transaction details				
		transactionDate = line[13]	
		amount = line[14]
		SUB_ID = line[20]	
		transactionId = getTransaction(CMTEID, donorId, amount, SUB_ID)
		if not transactionId:
			Values = [CMTEID, donorId, amount, SUB_ID]
			SQLCommand = ("INSERT INTO transactions " "(CMTE_ID, donor, amount, SUB_ID) "  "VALUES (?,?,?,?)")
			cursor.execute(SQLCommand,Values)
			connection.commit()
			transactionId = getTransaction(CMTEID, donorId, amount, SUB_ID)
connection.close()
print count
