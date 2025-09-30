def class_standing(num):
    if num < 7:
        return "Freshman: {} credits".format(num)
    elif num >= 26:
        return "Senior: {} credits".format(num)
    elif num >= 16:
        return "Junior: " + str(num) + " credits"
    else:
        return "Sophomore: " + str(num) + " credits"

def main():
    print(class_standing(10))
    print(class_standing(3))
    print(class_standing(27))
    print(class_standing(18))

main()
