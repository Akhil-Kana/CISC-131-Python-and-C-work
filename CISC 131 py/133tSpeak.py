def to133t(string):
    text = ""
    for i in range(len(string)):
        if string[i] == "e" or string[i] == "E":
            text += "3"
        elif string[i] == "s" or string[i] == "S":
            text += "5"
        elif string[i] == "o" or string[i] == "O":
            text += "0"
        else:
            text += string[i]
    return text

print(to133t("Hello world!"))
