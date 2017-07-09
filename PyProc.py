
"""
name: EYUP TEKKANAT
student number: 2426086

in this program; opened a data file from parameter file and detected its format. 
Then file parsed line by line and prepared metadata to write on meta data file from parameter file.
Used regular expression library to find numeric fields and sys library to run on command line.

"""


import json
import re
import sys




with open(sys.argv[1]) as f:
    data = json.load(f)
    print data
    

file_path = data["infile"]


out_file = data["metafile"]



seperator = 0 


if  file_path.lower().endswith(('.csv')) or file_path.lower().endswith(('.txt')):
    if  file_path.lower().endswith(('.csv')):
        print "this is a csv file"    
        seperator = ","
    else:
        print "this is a txt file"
        seperator = "\t"
        
    with open(file_path, 'r') as final:
        row_counter = 0
        field_counter = 0
        header = bool 
        dict_output = {}
        unique_array = []
        for row in final:
            list1 = []  # a list to process data line by line
            list2 = []  #final list
            
            
            list1 = (row.rstrip().split(seperator))
            i = 0
            for y in list1:
                
                
                
                if [y] not in unique_array and len(unique_array) != len(list1):
                    unique_array.append([y])
                
                if y not in unique_array[i]:
                    if re.findall(r"([0-9.]*[0-9]+)", str(list1[i])): 
                        unique_array[i].append(int(list1[i])) 
                    else:
                        unique_array[i].append(list1[i]) 

                
                i += 1
            row_counter +=1
    for z in unique_array:
        
        if str(z[1]).isdigit():
            list2.append({"name" : z[0],"type" : "numeric", "max": max(z[1::]), "min": min(z[1::])})
        else:
            list2.append({"name" : z[0],"type" : "string", "unique_vslue": len(z[1::])})

    field_counter = len(list1)            
    
    if len(z[0]) == len(list1) and str(z[0]).isdigit() :
        header = False
    else:
        header = True
        row_counter -=1
    
    
    dict_output = {"format": "tabular", "fields": list2, "numrows": row_counter,
                   "header": header,"seperator": seperator, "numfields": field_counter , "infile": file_path }
    
    print dict_output
    
    with open(out_file, 'w') as outfile:
        json.dump(dict_output, outfile)
   

elif file_path.lower().endswith(('.json')):
    print "this is a json file"
   
    
    with open(file_path) as final:
        row_counter = 0
        unique_array = []
        for v in final:
            dict1 = {} 
            dict1 = json.loads(v.rstrip())
            #print dict1
            field_counter =  len(dict1.keys())         # how many fields in a row
            list1 = []                                 # final list json format        
            row_counter +=1
            i = 0
            for y in dict1: 
                if [y] not in unique_array and len(unique_array) != len(dict1.keys()):
                    unique_array.append([y])
                
                if unique_array[i][0] == y and dict1[y] not in unique_array[i]:
                    unique_array[i].append(dict1[y])                      
                
                x = []
                x = re.findall(r"([0-9.]*[0-9]+)", str(dict1[y]))   #regex to find it's numeric or not
    
                if len(x)> 0 :
                    list1.append({"name" : y,"type" : "numeric", "max": max(unique_array[i][1::]), "min": min(unique_array[i][1::])})
                else:
                    list1.append({"name" : y,"type" : "string", "unique_vslue": len(dict1[y])})  
                i += 1 
                
    
    dict_output = {"format": "json", "fields": list1, "numrows": row_counter,
                   "seperator": seperator, "numfields": field_counter , "infile": file_path }
    
    print dict_output
    
    with open(out_file, 'w') as outfile:
        json.dump(dict_output, outfile)

                
   