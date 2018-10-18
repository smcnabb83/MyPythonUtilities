import csv
import sys
import re

if len(sys.argv) != 4:
    print("This command takes 3 arguments, the first for the table you want\n"
          "to write to, the second points to the csv file representing\n"
          "your table, and the third is an output file\n\n"
          "usage: py updatecsvtosql.py (table name) (input file name) (output file name)")
    exit()

tableName = sys.argv[1]
fileName = sys.argv[2]
outFileName = sys.argv[3]

rownum = 0
tableColumns = []
key = ""
retQuery = ""

with open(fileName) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if rownum == 0:
            tableColumns = row[:-1]
            key = row[-1]
            rownum += 1
        else:
            retQuery += f'UPDATE {tableName} SET\n'
            for table, vals in zip(tableColumns, row[:-1]):
                rowval = vals.rstrip().replace("\'","\'\'")
                retQuery += f"\t[{table}] = \'{rowval}\',\n"
            retQuery = retQuery[:-2]
            retQuery += f'\nWHERE {key} = \'{row[-1].rstrip()}\''
            retQuery += ';\n\n'
with open(outFileName, mode='w+') as outFile:
    outFile.write(retQuery)
            
            
