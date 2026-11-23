import json #import json module

def load_data(path):
    try:
        with open (path, 'r') as file:
            data = json.load(file) #open the file and load the data
        return data
    except:
        return "failed to load data" #error message if data load fails

def write_data(path, key, data): #write data to dict func, takes key and data - temporary function to establish JSON handling
    try:
        with open (path, 'r') as file:
            loaded_data = json.load(file) #open the file and load the data
    except:
        return "failed to load data" #error message if data fails to laod

    loaded_data[key] = data

    try:
        with open (path, 'w') as file: #open file in write mode
            json.dump(loaded_data, file) #write over existing data with new data
        return 'data written'
    except:
        return 'data could not be written' #error message if data could be loaded but new data not written
        
print (write_data('stage_data.json', 'Stage 3', ['Stage 3', 10, "Shaun's Garden"] ))
