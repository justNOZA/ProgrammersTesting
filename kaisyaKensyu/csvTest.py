import csv

asahikawa=open('asahikawa_zip.csv')
asahikawa_reader=csv.reader(asahikawa)
for row in asahikawa_reader:
	if row[2] =='788205':
		print(row[6],row[7],row[8])

asahikawa.close()
