'''
how to use a dictionary:

id_to_name = {
    "1": "jamie"
    "2": "shaun"
    "3": "akeel"
    "4": "thomas"
}
this would set up a dictionary, the data items stored in it can be lists! the first one is the primary key sort of

VIEW
name = id_to_name["1"]

UPDATE
id_to_name.update({"1": "john"}})

ADD
id_to_name.update({"5": "rachel"})
if there is no item to update then it will create a new one

REMOVE
id_to_name.pop("1")



to use json, use the functions jamie put on main, will have them in another file ../app/json_handling.py

it maps directly to a dictionary
'''

import json
from app.json_handling import json_to_dict, dict_to_json
json_path = "vendor_data.json"
vendor_data = {}

def add_vendor(name, food_type, location):

    # invalid type
    try:
        name = str(name)
    except TypeError:
        print("vendor name must be a string")
        return False

    # name blank
    if name == " ":
        print("vendor name cannot be a blank character")
        return False

    # name already taken
    name_taken = view_vendor(name) # use index 0 to access the true or false part
    if name_taken[0] == True:
        print("vendor name already taken")
        return False

    # name is usable, add vendor to dictionary
    vendor_data = json_to_dict(json_path) # import all vendors from file
    try:
        vendor_data = dict(vendor_data)
    except TypeError: # failed to read data error
        print("error in loading vendor data from file")
        return False
    
    # no reading error occured    
    vendor_data.update({name: [name, food_type, location]}) # add new vendor
    write_result = dict_to_json(json_path, vendor_data) # write data back to file

    if write_result == "data written": # written successfully
        return True
    elif write_result == "failed to write data": # failed to write error
        print("error in writing vendor data to file")
        return False
    else: # completely unknown error
        print("unknown error in writing data to file")
        return False



def view_vendor():
    print()



def update_vendor():
    print()



def delete_vendor():
    print()