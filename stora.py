import csv

#vantar að biðja um skraar nafn

# svona opnar maður csv skrá og prentar út
with open('SAM02011.csv') as csvfile:
<<<<<<< HEAD
  thereader = csv.reader(csvfile, delimiter=';')
  for row in thereader:
    print(len(row))
    print(row)i
=======
    thereader = csv.reader(csvfile, delimiter=';')
    for row in thereader:
        print(len(row))
        print(row)
>>>>>>> origin/master
