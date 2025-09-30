def palindromeR(string):
    return len(string) == 0 or (string[0] == string[-1] and palindromeR(string[1:-1]))

print(palindromeR("racecarr"))
print(palindromeR("racecar"))
print(palindromeR("bal"))
print(palindromeR("hi"))
print(palindromeR("e"))
print(palindromeR(""))
print(palindromeR("bob"))
print(palindromeR("thanksgiving"))
