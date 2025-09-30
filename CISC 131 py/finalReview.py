
#recursion

def allDigits(string):
    if len(string) == 0:
        return True
    elif (ord(string[0]) > 57 or ord(string[0]) < 48):
        return False
    else:
        return allDigits(string[1:])

print(allDigits("12a3"))
print(allDigits("1243"))
