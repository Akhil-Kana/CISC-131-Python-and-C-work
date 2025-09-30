def transcribe(sequence):
    sequence = sequence.replace("A", "U")
    sequence = sequence.replace("T", "A")
    sequence = sequence.replace("C", "g")
    sequence = sequence.replace("G", "C")
    sequence = sequence.upper()
    return sequence

def transcribe2(dna):
    string = ""
    for i in range(len(dna)):
        if dna[i] == "A":
            string += "U"
        elif dna[i] == "T":
            string += "A"
        elif dna[i] == "C":
            string += "G"
        elif dna[i] == "G":
            string += "C"
    return string

def translate(sequence):
    for i in range(0, len(sequence), 3):
        for j in range(3):
            print(sequence[j+i], end="")
        print("")


print(transcribe("AAATAGCCAGGTACCAATGA"))
print(transcribe2("AAATAGCCAGGTACCAATGA"))
translate("AAATAGCCAGGTACCAATGAG")
