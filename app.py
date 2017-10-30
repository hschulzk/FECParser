import csv
import datetime as dt

def now():
	return dt.datetime.now()
#def makePseudoTableRow(oneLine):
	# Accepts one line from the CSV and returns it as an array 


with open('indiv_header_file.csv') as csvFile:
	for line in csvFile:
		print(line)

# fhand = open('itcont.txt')
# count = 0 
# for line in fhand:
# 	count = count + 1
# 	if count > 1000: break
# 	print(line)

with open('itcont.txt') as csvFile:
	starttime = now()
	count = 0
	#0
	cmte_id = dict()
	
	# 7
	contributor = dict()
	# 8
	city = dict()
	# 9
	state = dict()
	# 10
	zipCode = dict()
	# 11
	employer = dict()
	# 12
	occupation = dict()
	# 14
	donation = dict()

	fieldnames = ['CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI','IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY','STATE','ZIP_CODE','EMPLOYER','OCCUPATION','TRANSACTION_DT','TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD','MEMO_TEXT','SUB_ID']
	reader = csv.reader(csvFile, delimiter='|')
	
	for line in reader:
		if (count > 10000): break
		#print(line)
		count = count + 1
		cmte_id.update({line[20]:line[0]})

		
		# cmte_id.update({line[20]:line[0]})

		# contributor.update({line[20]:line[7]})
		# city.update({line[20]:line[8]})
		# state.update({line[20]:line[9]})
		# zipCode.update({line[20]:line[10]})
		# employer.update({line[20]:line[11]})
		# occupation.update({line[20]:line[12]})

		donation.update({line[20]:line[14]})
print(now() - starttime)
print(count)
print(cmte_id)
# printCount = 0

# for key in donation:
# 	printCount = printCount + 1
# 	print(str(donation[key]) + ' ' + employer[key] + ' ' + occupation[key])
# print(printCount)