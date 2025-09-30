"""
color_dict = {"Max":"blue", "Maria":"blue", "Kayden":"blue"}
color_dict["Max"] = "green"
color_dict["Thy"] = "purple"
del color_dict["Max"]
for i in color_dict:
    print(i, color_dict[i])
"""

"""
Infectious Disease Spread

def main():
#sim param
    num_people = 1000
    num_days = 100
    percent_distancing = 0.0
    distance_contacts = 2
    nondistance_contacts = 25
    disease = {
        "spread_probability": 0.02,
        "contagious_period": 14
    }
    disease["spread_probability"] = int(input("Input spread prob: "))/100

people = [
    {
        "status": "infected",
        "status_change_time": 0,
        "num_contacts": nondistance_contacts
    }
]
for _i in range(0, num_nondistancing):
    person = {
        "status": "susceptible",
        "status_change_time": 0,
        "num_contacts": nondistance_contacts
    }
    person.append(person)
for _i in range(0, num_distancing):
    person = {
        "status": "susceptible",
        "status_change_time": 0,
        "num_contacts": distance_contacts
    }
    person.append(person)
    
main()
"""