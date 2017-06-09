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

def getCommitteeId(CMTEID):
	SQLCommand = ("SELECT id " "FROM committees " "WHERE cmte_id = ?") 
	Values = [CMTEID]
	cursor.execute(SQLCommand,Values)
	results = cursor.fetchone()
	if results:
		return results[0]
	else:
		return False

cursor = connection.cursor()
with open('cm.txt', 'r') as fhand:
	for line in fhand:
		count += 1
		line = line.strip()
		line = line.split('|')
		#committeeInfo
		CMTEID = line[0]
		CMTENAME = line[1]
		#If committeeID is in database, return the ID. Else, insert it and return that id
		committeeId = getCommitteeId(CMTEID)
		if not committeeId:
			Values = [CMTEID, CMTENAME]
			SQLCommand = ("INSERT INTO committees " "(cmte_id, cmte_name) " "VALUES (?, ?)")
			cursor.execute(SQLCommand,Values)
			connection.commit()
		else:
			Values = [CMTENAME, CMTEID]
			SQLCommand = ("UPDATE committees " "SET cmte_name = ? " "WHERE cmte_id = ?")
			cursor.execute(SQLCommand,Values)
			connection.commit()
connection.close()
print count
