import json #import json module

with open ('stage_data.json') as file:
    data = json.load(file) #open the file and load the data
    
print (data)