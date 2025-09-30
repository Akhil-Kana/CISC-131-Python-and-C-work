def toUpper(lowC):
    x = ord(lowC)
    y = (bin(x) - 0b100000)
    z = chr(y)
    return z

print(toUpper('a'))
