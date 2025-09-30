def allPlus(my_string):

    for index in range(len(my_string)):

        if my_string[index] != '+':

            return False

    return True
        
print(allPlus("++++++"))