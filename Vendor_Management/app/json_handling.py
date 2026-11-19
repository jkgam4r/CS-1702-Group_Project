import json

def json_to_dict(path): # importing the data from the json into the dictionary
    try:
        with open (path, 'r') as file: #open file in read mode
            data = json.load(file) # read file into data
        return data # return data if successfully done
    except:
        return "failed to load data" # return error message
    

def dict_to_json(): # saving any updated data back to the json
    # dont actually understand how this one works atm, will add it in later
    print()