# connect to database
database = {}

response_codes = {
    0: "Success",
    1: "Invalid",
    2: "Redundant"
}

# add people to bus
    # check if user already added to bus
        # if so, return error code
        # else, return success code


import json

def signUp(info): # returns: 1 - invalid entry, 2 - pass # already on list, 0 - success
    first_name = info["first_name"]
    last_name = info["last_name"]
    pass_number = info["pass_number"]
    location = info["location"]

    if first_name == "First name" or last_name == "Last name" or pass_number == "Pass #":
        return 1

    if pass_number in database.keys():
        return 2

    else:
        database[pass_number] = {
            "first_name": first_name,
            "last_name":  last_name,
            "location":   location
        }
        return 0
