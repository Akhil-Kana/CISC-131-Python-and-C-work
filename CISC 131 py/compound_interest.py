def main():
    #test the timeDouble function
    print("Testing timeDouble(10,1):")
    timeDouble(10, 1)
    print("Testing timeDouble(.05,1):")
    timeDouble(.05, 1)
    #test the timeDouble2 function
    print("Testing timeDouble2(10,1):")
    timeDouble2(10, 1)
    print("Testing timeDouble(.05,1):")
    timeDouble(.05, 1)

def timeDouble(interest_rate, compound_times):
    """
    See the assignment for a description.
    """
    interest_rate = interest_rate/100
    for i in range(1, 101):
        amount = 10*(1 + interest_rate/compound_times)**(compound_times*i)
        if amount > 20:
            print("It takes {:d} years to double".format(i))
            return
    print("It takes more than 100 years to double.")

def timeDouble2(interest_rate, compound_times):
    """
    See the assignment for a description.
    This function does the same thing as above but
    does not use a return statement.
    """
    interest_rate = interest_rate/100
    has_doubled = False
    for i in range(1, 101):
        amount = 10*(1 + interest_rate/compound_times)**(compound_times*i)
        if amount > 20 and not has_doubled:
            print("It takes {:d} years to double".format(i))
            has_doubled = True
    if not has_doubled:
        print("It takes more than 100 years to double.")
main()
