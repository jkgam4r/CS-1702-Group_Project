import json

def json_to_dict(path): # importing the data from the json into the dictionary
    try:
        with open (path, "r") as file: # open file in read mode
            data = json.load(file) # read file into data
        return data # return data if successfully done
    except:
        return "failed to read data" # return error message
    

def dict_to_json(path, data): # saving any updated data back to the json
    try:
        with open (path, "w") as file: # open file in write mode
            json.dump(data, file) # overwrite old data with new data
        return "data written" # return message if successfully done
    except:
        return "failed to write data" # return error message