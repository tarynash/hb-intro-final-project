import csv

with open('christmas_songs.csv') as csvfile:
	christmas_test = csv.reader(csvfile, delimiter=" ",quotechar="|")
	for row in christmas_test:
		print ",".join(row)
		
