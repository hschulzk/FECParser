fhand = open('cm.txt')
count = 0
for line in fhand:
	line = line.strip()
	words = line.split('|')
	print "Committee ID: ", words[0]
	count += 1
	if count > 10:
		break