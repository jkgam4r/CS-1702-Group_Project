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
- vendor name (yes its a duplicate but who its okay)
- food type (hot dogs, burgers, etc)
- location (stage area, same as the ID for a stage like stage_1 or however jamie is going to do it)

vendor data = [vendor name x, food type, location]



functions:

add vendor (name, food type, location)
- if name already exists, return false
- else, create a new vendor
- add to main dictionary and json
- return true if done successfully

view vendor (name)
- check if vendor by name exists
- if no, return list with 1 element with false, can catch this later using len(list)
- if yes, return the associated data from dictionary in a nested list [bool, vendor data] yk

update vendor (name, data as list)
- check if vendor exists
- if no, return false
- if yes, update data values
- return true if done successfully

delete vendor (name)
- check if vendor exists
- if no, return false
- else, get confirmation from user
- check confirmation
- if confirmation is wrong, return false
- else, delete data from dictionary and json
- return true if done successfully



remember to use:
- try (can cause error), except (name and handle error), else (if no error), finally (always run this bti)
- loops on taking inputs (force user to actually input something rather than just press enter)
- pytest ()
'''