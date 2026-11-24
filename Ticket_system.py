import json
def load_ticket_data():
    try:
        with open("Ticket_Data.json", "r") as file:
            data = json.load(file)
            return data
    except:
        return "File not found or error in loading data"

def add_ticket(ticket_data):
    try:
        with open("Ticket_Data.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(ticket_data)

    with open("Ticket_Data.json", "w") as file:
        json.dump(data, file)


print("1. Load Ticket Data \n2. Add Ticket Data")