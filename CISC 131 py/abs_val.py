def absVal(num):
    if num > 0:
        print("The number is greater than 0!")
        return abs(num)
    elif num < 0:
        print("The number was less than 0!")
        return abs(num)
    else:
        print("The number is equal to 0!")
        return abs(num)

def main():
    print(absVal(-9))
    print(absVal(7))
    print(absVal(0))

main()