import json #import json module


def load_data(path):
    try:
        with open (path) as file:
            data = json.load(file) #open the file and load the data
        return data
    except:
        return "Failed to load data"


print (load_data('stage_data.json'))