def alp():
    alp_list = []
    for i in range(26):
        alp_list += chr(97+i)
    return alp_list

def alp2():
    alp_list = []
    for i in range(26):
        alp_list.append(chr(97+i))
    return alp_list

print(alp())
print(alp2())
