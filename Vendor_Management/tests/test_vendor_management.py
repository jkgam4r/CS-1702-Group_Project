'''
how to make tests!

make a fn called test_ then the fn name WITH NO ARGUMENTS
call the fn from other file with argument being tested (valid, boundary, erroneous)
assert result is expected

it should look like this:

def test_get_animal_noise():
    result = get_animal_noise("Cat")
    assert result == "Meow"
'''

import pytest
from app.main import add_vendor, view_vendor, update_vendor, delete_vendor


# ADD VENDOR
def test_valid_add_vendor():
    try:
        result = add_vendor("Burger Bros", "Burgers", "Stage1") # expected values
        assert result == True # vendor was added successfully
    finally:
        delete_vendor("Burger Bros", True) # test should pass, deleting vendor so the test can be run again

def test_boundary_add_vendor():
    result = add_vendor(" ", " ", " ") # unexpected values
    assert result == False # names have to contain characters

def test_erroneous_add_vendor():
    result = add_vendor(1, None, [1,2,3,4]) # someone trying to break the program
    assert result == False # invalid data, None should give a type error i think and the list is just ridiculous lol


# VIEW VENDOR
def test_valid_view_vendor():
    result = view_vendor("Hot Dog Men") # default testing vendor, add this to dict and json when creating them
    assert result == [True, ["Hot Dog Men", "Hot Dogs", "Stage1"]] # vendor was found successfully, and information shown

def test_boundary_view_vendor():
    result = view_vendor(" ") # no vendor is allowed to have this name but it is a valid string
    assert result == [False, ""] # invalid name for vendor, therefore shouldnt exist, therefore shouldnt be found

def test_erroneous_view_vendor():
    result = view_vendor([1,2,3,4]) # complete wrong data type, to be handled by try except
    assert result == [False, ""] # vendor not found bc they cant be called strings, kinda obvious


# UPDATE VENDOR
def test_valid_update_vendor():
    try:
        result = update_vendor("Hot Dog Men", ["Vegan Hot Dog Men", " Vegan Hot Dogs", "Stage2"]) # expected and valid values
        assert result == True # values updated successfully
    finally:
        update_vendor("Vegan Hot Dog Men", ["Hot Dog Men", "Hot Dogs", "Stage1"]) # test should pass, changing the data back

def test_boundary_update_vendor():
    result = update_vendor(" ", ["Spud Sisters", "Jacket Potatoes", "Stage3"]) # vendors cannot be called this, therefore shouldnt exist, therefore shouldnt be found
    assert result == False # no vendor found to update values for

def test_erroneous_update_vendor():
    result = update_vendor([1,2,3,4], "hello") # completely invalid arguments
    assert result == False # a vendor cant be called a list, so wont be found


# DELETE VENDOR
def test_valid_delete_vendor():
    try:
        result = delete_vendor("Hot Dog Men", True) # valid vendor with confirmation
        assert result == True # vendor deleted successfully
    finally:
        add_vendor("Hot Dog Men", "Hot Dogs", "Stage1") # the test should pass, so need to put the vendor back

def test_boundary_delete_vendor():
    result = delete_vendor("Hot Dog Men", "No") # valid vendor name, invalid confirmation tho
    assert result == False # vendor not deleted

def test_erroneous_delete_vendor():
    result = delete_vendor([1,2,3,4], [1,2,3,4]) #completely invalid arguments
    assert result == False # vendor not deleted