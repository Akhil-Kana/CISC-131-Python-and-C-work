"""
CISC 131
IN CLASS: Infectious Disease Spread
"""
import turtle
import random

black = "#000000"
red = "#EA1010"
green = "#32A852"
blue = "#2A35C9"

def main():

    # simulation parameters
    num_people = 1000            # keep this constant
    num_days = 100               # keep this constant
    percent_distancing = 0.0     # change this to see the effect on the simulation
    distance_contacts = 2        # change this to see the effect on the simulation
    nondistance_contacts = 25    # change this to see the effect on the simulation
    disease = {                  # change this to see the effect on the simulation
        "spread_probability": 0.02,
        "contagious_period": 14
    }

    # do simulation
    num_distancing = int(num_people * percent_distancing)
    num_nondistancing = num_people - num_distancing - 1
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
        people.append(person)
    for _i in range(0, num_distancing):
        person = {
            "status": "susceptible",
            "status_change_time": 0,
            "num_contacts": distance_contacts
        }
        people.append(person)

    susceptible_list = []
    infected_list = []
    recovered_list = []
    for _i in range(num_days):
        for j in range(num_people):
            people[j]["status_change_time"] = people[j]["status_change_time"] + 1
            if (people[j]["status"] == "infected" and
                    people[j]["status_change_time"] >= disease["contagious_period"]):
                people[j]["status"] = "recovered"
            if people[j]["status"] == "infected":
                for _k in range(people[j]["num_contacts"]):
                    person_idx = random.randint(0, num_people - 1)
                    if people[person_idx]["status"] == "susceptible":
                        does_infect = random.uniform(0, 1.0)
                        if does_infect <= disease["spread_probability"]:
                            people[person_idx]["status"] = "infected"
                            people[person_idx]["status_change_time"] = 0

        #THE CODE BELOW HAS BEEN MODIFIED
        #You will write the countPeople function below
        count = countPeople(people)
        susceptible_list.append(count["susceptible"])
        infected_list.append(count["infected"])
        recovered_list.append(count["recovered"])


    graphInfectiousSpread(susceptible_list, infected_list, recovered_list)

def countPeople(people):
    #WRITE YOUR CODE HERE FOR PROBLEM 3
    c_inf = 0
    c_susc = 0
    c_rec = 0
    for person in people:
        if person["status"] == "infected":
            c_inf += 1
        elif person["status"] == "susceptible":
            c_susc += 1
        elif person["status"] == "recovered":
            c_rec += 1
    return {"infected": c_inf, "susceptible": c_susc, "recovered": c_rec}

def graphInfectiousSpread(susceptible_list, infected_list, recovered_list):
    pen = turtle.Turtle()
    turtle.Screen().setup(width=800, height=800)
    turtle.Screen().setworldcoordinates(-10, -100, 110, 1100)
    turtle.Screen().title("Infectious Disease Spread")

    # set pen to draw black lines
    pen.up()
    pen.color(black)

    # draw horizontal graph line
    pen.goto(0, 0)
    pen.down()
    pen.goto(100, 0)
    pen.up()

    # draw vertical graph line
    pen.goto(0, 0)
    pen.down()
    pen.goto(0, 1000)
    pen.up()

    # draw days (horizontal axis)
    for day in range(0, 110, 10):
        pen.goto(day - 2, -50)
        pen.write("{:^3d}".format(day), font=("Courier New", 16, "normal"))

    # draw number of people (vertical axis)
    for num in range(0, 1100, 100):
        pen.goto(-8, num - 16)
        pen.write("{:4d}".format(num), font=("Courier New", 16, "normal"))

    # draw legend
    drawRect(pen, 10, 1075, 4, 40, black, blue)
    pen.color(black)
    pen.goto(16, 1040)
    pen.write("Susceptible", font=("Arial", 18, "normal"))

    drawRect(pen, 45, 1075, 4, 40, black, red)
    pen.color(black)
    pen.goto(51, 1040)
    pen.write("Infected", font=("Arial", 18, "normal"))

    drawRect(pen, 80, 1075, 4, 40, black, green)
    pen.color(black)
    pen.goto(86, 1040)
    pen.write("Recovered", font=("Arial", 18, "normal"))

    # draw susceptible line
    pen.color(blue)
    pen.goto(0, susceptible_list[0])
    pen.down()
    for i in range(1, len(susceptible_list)):
        pen.goto(i, susceptible_list[i])
    pen.up()

    # draw infected line
    pen.color(red)
    pen.goto(0, infected_list[0])
    pen.down()
    for i in range(1, len(infected_list)):
        pen.goto(i, infected_list[i])
    pen.up()

    # draw recovered line
    pen.color(green)
    pen.goto(0, recovered_list[0])
    pen.down()
    for i in range(1, len(recovered_list)):
        pen.goto(i, recovered_list[i])
    pen.up()
    turtle.done()

def drawRect(pen, x, y, width, height, border, fill):
    pen.up()
    pen.color(border)
    pen.fillcolor(fill)
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.goto(x + width, y)
    pen.goto(x + width, y - height)
    pen.goto(x, y - height)
    pen.goto(x, y)
    pen.end_fill()
    pen.up()

main()
