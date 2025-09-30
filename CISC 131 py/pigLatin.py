def pigSplit(string):
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "y":
            return i
    return -1

def pigLatin(string):
    if pigSplit(string) == -1:
        return "Not a valid word"
    elif pigSplit(string) == 0:
        return string + "yay"
    else:
        return string[pigSplit(string) : len(string)] + string[pigSplit(string)-1] + "ay"

print(pigLatin("hello"))
print(pigLatin("sandwich"))
