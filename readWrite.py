# fhand = open('itcont.txt')

with open('itcont.txt', 'r') as content_file:
	content = content_file.read()
	content = content.replace(",", " ")
	content = content.replace("|", ",")
with open('transactions.csv','w') as ofh:
    ofh.write(content)
print content