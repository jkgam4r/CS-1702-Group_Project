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



def view_vendor(name):
    try:
        viewing_vendor = []
        viewing_vendor = vendor_data[name]
    except KeyError: # name not found in dictionary
        print("vendor not found in dictionary")
        return_list = [False, ""]
        return return_list # return false and blank
    else: # name was found in dictionary
        return_list = [True, viewing_vendor]
        return return_list # return true and associated data



def update_vendor(name, new_data: list):
    # if vendor exists
    vendor_exists = view_vendor(name) # use index 0 to access the true or false part
    if vendor_exists[0] == False: # vendor not found
        print("vendor cannot be updated as it doesnt exist")
        return False

    # vendor does exist
    vendor_data = json_to_dict(json_path) # import all vendors from file
    try:
        vendor_data = dict(vendor_data)
    except TypeError: # failed to read data error
        print("error in loading vendor data from file")
        return False

    # data loaded correctly
    vendor_data.update({name: [new_data]}) # update vendor
    write_result = dict_to_json(json_path, vendor_data) # write data back to file

    if write_result == "data written": # written successfully
        return True
    elif write_result == "failed to write data": # failed to write error
        print("error in writing vendor data to file")
        return False
    else: # completely unknown error
        print("unknown error in writing data to file")
        return False



def delete_vendor(name, confirmation):
    # if vendor exists
    vendor_exists = view_vendor(name) # use index 0 to access the true or false part
    if vendor_exists[0] == False: # vendor not found
        print("vendor cannot be deleted as it doesnt exist")
        return False

    # vendor does exist
    # is confirmation valid
    if confirmation == True:
        #delete vendor in sub func
        vendor_deleted = delete_vendor_confirmed(name) # returns bool if actually did it
        if vendor_deleted == True:
            return True
        elif vendor_deleted == False:
            print("vendor not deleted, error")
            return False
        else:
            print("error not deleted, error")
            return False

    #dont delete vendor
    elif confirmation == False:
        print("give valid confirmation to delete vendor")
        return False
    else: 
        print("null value error")
        return False



def delete_vendor_confirmed(name):
    # load data from file
    vendor_data = json_to_dict(json_path) # import all vendors from file
    try:
        vendor_data = dict(vendor_data)
    except TypeError: # failed to read data error
        print("error in loading vendor data from file")
        return False

    # remove vendor from dict
    vendor_data.pop(name)

    # store data back in file
    write_result = dict_to_json(json_path, vendor_data) # write data back to file

    if write_result == "data written": # written successfully
        return True
    elif write_result == "failed to write data": # failed to write error
        print("error in writing vendor data to file")
        return False
    else: # completely unknown error
        print("unknown error in writing data to file")
        return False