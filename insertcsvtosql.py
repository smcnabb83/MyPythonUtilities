import csv
import sys
import re

#The csv file you feed into the script needs to have the 
#first row be column headers, and subsequent rows can be data. 
#If something is not explicitly found to either be numeric
#or null, it is sent as a string.

if len(sys.argv) != 4:
    print("This command takes 3 arguments, the first for the table you want\n"
          "to write to, the second points to the csv file representing\n"
          "your table, and the third is an output file\n\n"
          "usage: py csvtosql.py (table name) (input file name) (output file name)")
    exit()

tableName = sys.argv[1]
fileName = sys.argv[2]
outFileName = sys.argv[3]

isnull = re.compile(r"^\s*\'*null\'*\s*$", re.IGNORECASE)
isnumeric = re.compile(r"^\s*\'*\d+(?:\.\d+){0,1}\'*\s*$", re.IGNORECASE)

rownum = 0
retQuery = f'INSERT INTO {tableName} ('

with open(fileName) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if rownum == 0:
            retQuery += ', '.join(row).strip('\n') + ")\n VALUES \n"
            rownum += 1
        else:
            row[:] = [x.strip(' \t\n\r') for x in row]
            row = list(filter(None, row))
            if not row:
                continue
            
            row[:] = ["\'"+x+"\'" for x in row]
            row = map(lambda x:x.strip("\'").lower() if isnull.match(x) or isnumeric.match(x) else x, row)
            retQuery += "(" + ','.join(row)+"),\n"
            
retQuery = retQuery[:-2]
retQuery += ";"

with open(outFileName,mode='w+') as outFile:
    outFile.write(retQuery)



