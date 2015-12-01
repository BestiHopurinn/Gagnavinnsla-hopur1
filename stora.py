import csv

with open('nafnid a skranni') as csvfile
  thereader = csv.reader(csvfile)
  for row in thereader
    print(row)
