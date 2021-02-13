import csv
import re

regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

with open('Responses.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)

 for row in data:

     if(re.search(regex,row['Email'])):
         print(row['ID']+ "         <------->          Valid Email\n")
     else:
         print(row['Email'].strip() + "         <------->          Invalid Email\n")
