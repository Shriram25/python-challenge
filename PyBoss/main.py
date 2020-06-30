import os
import csv

from datetime import datetime

csvpath = os.path.join('Resources','employee_data.csv')
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    

    csv_header = next(csvreader)
    print(csv_header)
    convertedrow = []
    outputfile =  open("output.txt","w")
    for row in  csvreader:
       
        id = row[0]
        convertedrow.append(id)
        name = row[1]
        names = name.split(" ",1)
       
        convertedrow.append(names[0])
        convertedrow.append(names[1])
        dob = row[2]
        convertdate = datetime.strptime(dob,"%Y-%m-%d")
        newdate = convertdate.strftime("%m/%d/%Y")
       
        convertedrow.append(newdate)
        
        ssn = row[3]
        convertedssn = "***-**-"+str(ssn[7:11])
        convertedrow.append(convertedssn)
        state = row[4]
        abbstate = us_state_abbrev[state]
        convertedrow.append(abbstate)
        print(convertedrow)
        
        outputfile.write(convertedrow[0]+","+convertedrow[1]+","+convertedrow[2]+","+convertedrow[3]+","+convertedrow[4]+"\n")



        convertedrow.clear()
    outputfile.close()


     


