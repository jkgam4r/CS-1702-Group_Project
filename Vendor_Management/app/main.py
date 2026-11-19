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

def add_vendor():
    print()

def view_vendor():
    print()

def update_vendor():
    print()

def delete_vendor():
    print()