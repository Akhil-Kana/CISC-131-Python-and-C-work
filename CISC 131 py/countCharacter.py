def main():
    name = "pride&prejudice.txt"
    file_ref = open(name, 'r')
    num_lines = 0
    num_para = 0
    num_char = 0
    num_word = 0
    next_line = file_ref.readline()
    while next_line != "":
        num_lines = num_lines + 1
        num_char = num_char + len(next_line)
        if next_line[0] != "\n":
            num_word = num_word + countWords(next_line)
        else:
            num_para = num_para + 1
        next_line = file_ref.readline()
    file_ref.close()
    print("The number of lines is", num_lines)
    print("The number of paragraphs is", num_para)
    print("The number of characters is", num_char)
    print("The number of words is", num_word)

def countWords(input_str):
    """
    This function returns the number of words in input_str
    """
    #1. Change all groups of spaces so they're only
    # a single space. E.g. " hi bye " becomes
    #" hi bye ".
    for _i in range(len(input_str)):
        input_str = input_str.replace(" ", " ")
    #2. Remove any spaces at the beginning and end of the
    #string
    input_str = input_str.strip()
    #3. Count the number of spaces. This is one less than
    #the number of words so we then add 1.
    num_words = input_str.count(" ") + 1
    #4. Return the answer.
    return num_words

main()
