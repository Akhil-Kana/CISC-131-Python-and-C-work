"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520)
"""

def prettyPrint(lst, indent):
    """
    This function takes a list and prints it in a "pretty" format
    """
    print("[")
    for i in range(len(lst)):
        print(" " * (4 * (indent + 1)), end="")
        if isinstance(lst[i], str):
            print('"' + str(lst[i]) + '"', end="")
        elif isinstance(lst[i], list):
            prettyPrint(lst[i], indent + 1)
        else:
            print(lst[i], end="")
        if i < len(lst) - 1:
            print(",")
        else:
            print("")
    print(" " * (4 * (indent)) + "]", end="")

prettyPrint([1, "hi", [3.14, 42, 0.0], [[1,2], [3,4]], "last"], 0)
