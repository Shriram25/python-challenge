import os
import csv
from datetime import datetime

csvpath = os.path.join('Resources','employee_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)
    print(csv_header)
    convertedrow = []
    for row in csvreader:
        print(row)
        name = row[1]
        names = name.split(" ",1)
        print(names)
        convertedrow.append(names)
        dob = row[2]
        convertdate =  datetime.strptime(dob,"%Y-%m-%d")
        newdate =convertdate.strftime("%m/%d/%y")
        print(newdate)
        convertedrow.append(newdate)
        print(convertedrow)
        ssn = row[3]
        print(ssn)

