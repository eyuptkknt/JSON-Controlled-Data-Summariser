import re 
        
import csv
from string import rstrip
from _sqlite3 import Row
with open('C:/Users/eyup/Desktop/merchant_list12.csv', 'rb') as f:
    reader = csv.reader(f)
    list_company = []
    
    list_example = ['PYPL ', 'CLOSE BROTHERS MOTOR FINANCE', 'CHELMSLEY WOOD SERVICE']
    for row in reader:
        
        if row[2] == "" or row[2] == "Merchant" :
             continue
        else:
            list_company.append(row[2])
            
    print list_company
    list_company.sort()
    print list_company
    
    if list_example[0][0] 
    print list_example[0][0]
    
    
    
    
     