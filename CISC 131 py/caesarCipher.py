import strings

def main():
    """
    This function tests all the other functions in our file.
    """
    print(convertNum("a"))
    print(convertNum("z"))
    print(convertLet(1))
    print(convertLet(24))
    print(encryptC("cat",2))
    print(decryptC("ecv",2))
    caesarBrute("yrggpwizurp")

def encryptC(input_str, shift):
    str_so_far = ""
    for i in range(len(input_str)):
        next_chr = input_str[i]
        current_num = convertNum(input_str[i])
        current_num = (current_num + shift)%26
        encrypt_chr = convertLet(current_num)
        str_so_far = str_so_far + encrypt_chr
    return str_so_far

def decryptC(input_str, shift):
    return encryptC(input_str, 26-shift)

def convertNum(input_chr):
    """
    Converts input_chr to a number using the mapping
    given (a -> 0, b->1, c-> 2, etc.)
    """
    ascci_val = ord(input_chr) - 97
    return ascci_val

def convertLet(input_num):
    """
    Converts input_chr to a letter using the mapping
    given (0->a, 1->b, 2->c, etc.)
    """
    return chr(97 + input_num)

def caesarBrute(input_str):
    for i in range(len(input_str)):
        print(decryptC(input_str, 26-i))

main()
