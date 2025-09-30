"""Binary ver"""
def toUpper(lower):
    return chr(ord(lower) - 0b100000)
  
"""Decimal ver"""
def toUpper2(low):
    return chr(ord(low) - 32) 

def toUpper3(lower_letter):
    if ord(lower_letter) < 97 or ord(lower_letter) > 122:
        return "ERROR: NOT LOWERCASE"
    else:
        return chr(ord(lower_letter) - 32)
    
print(toUpper('a'))
print(toUpper2('b'))
print(toUpper3('c'))
print(toUpper3('A'))
