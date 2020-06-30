import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)

    months = 0
    Average = 0
    changes = []
    changemonths = []

    value1 = 0
    value2 = 0
    rowcount = 0
    count = 0
    total = 0
    maxincrease = 0
    minincrease = 0
    for row in csvreader:
        
        months = months+1
        total = total+float(row[1])
        if rowcount == 0:
            value1 = float(row[1])
            rowcount = rowcount+1
        elif rowcount %2 ==0 and rowcount!=0 :
            value1 = float(row[1])
            changes.append(value1-value2)
            rowcount = rowcount+1
            changemonths.append(row[0])         
        else:
            value2 = float( row[1] )
            changes.append(value2-value1) 
            changemonths.append(row[0])
            rowcount = rowcount + 1
            count = count+1

average = sum(changes)/len(changes)
maxincrease = max(changes)
minincrease = min(changes)
maxloc =  changes.index(max(changes))
minloc =  changes.index(min(changes))
maxmonth = changemonths[maxloc]
minmonth = changemonths[minloc]
print("Financial Analysis")
print("------------------------")
print(f"Total months: {months}")
print(f"Total: ${round(total)}")
print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {maxmonth} (${round(maxincrease)})")
print(f"Greatest Decrease in Profits: {minmonth} (${round(minincrease)})")
outputfile =  open("output.txt","w")
outputfile.write("Financial Analysis\n")
outputfile.write("----------------------------\n")
outputfile.write(f"Total months: {months}\n")
outputfile.write(f"Total: ${round(total)}\n")
outputfile.write(f"Average Change: ${round(average,2)}\n")
outputfile.write(f"Greatest Increase in Profits: {maxmonth} (${round(maxincrease)})\n")
outputfile.write(f"Greatest Decrease in Profits: {minmonth} (${round(minincrease)})\n")
outputfile.close







