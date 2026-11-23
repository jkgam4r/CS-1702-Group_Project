'''
dictionary (to go in the json)
- vendor name (primary key)
- list of data

what it should look like
vendors json
    vendors = {
        vendor name 1 : [vendor data]
        vendor name 2 : [vendor data]
        }



whats in the list of data?
- vendor name (yes its a duplicate but its okay)
- food type (hot dogs, burgers, etc)
- location (stage area, same as the ID for a stage like stage_1 or however jamie is going to do it)

vendor data = [vendor name, food type, location]



functions:

add vendor (name, food type, location)
- if name already exists, return false
- if name is invalid type or " ", return false
- else, create a new vendor
- add to main dictionary and json
- return true if done successfully

view vendor (name)
- check if vendor by name exists
- if no, return list with 2 elements with false, then an empty string just to avoid error handling in the test fn
- if yes, return the associated data from dictionary in a nested list [bool, vendor data] yk

update vendor (name, data as list)
- check if vendor exists
- if no, return false
- if yes, update data values
- return true if done successfully

delete vendor (name, confirmation)
- check if vendor exists
- if vendor doesnt exist, return false
- else, get confirmation from user
- if confirmation is wrong, return false
- else, keep going
- delete data from dictionary and json
- return true if done successfully
DO THIS ONE BY HAVING AN OUTSIDE FUNCTION (delete_vendor) THAT DOES THE CHECKING IF VALID AND GETTING CONFIRMATION, THEN CALLS AN INSIDE FUNCTION TO ACTUALLY DO IT, CALL THIS SOMETHING ELSE IDK



remember to use:
- try (can cause error), except (name and handle error), else (if no error), finally (always run this bti)
- loops on taking inputs (force user to actually input something rather than just press enter)
- pytest ()
'''