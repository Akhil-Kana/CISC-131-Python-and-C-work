"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Ty Sandell (sand9838)
"""

def main():
    """
    This function calls the other functions within the file
    """
    applicants = readCsv("applicants.csv")
    ln1 = "Enter '1' to filter based on Overall GPA, '2' to filter based on Major GPA,"
    ln2 = " or '3' to filter based on our Custom Score: "
    while True:
        choice = input(ln1 + ln2)
        top_n = int(input("Enter the top number: "))
        if choice == "1" and top_n >= 0:
            lst = filterOverallGpa(applicants, top_n)
            break
        elif choice == "2" and top_n >= 0:
            lst = filterMajorGpa(applicants, top_n)
            break
        elif choice == "3" and top_n >= 0:
            lst = filterCustomScore(applicants, top_n)
            break
        else:
            print("That is not a valid number.")
    for i in range(top_n):
        var = lst[i]
        if choice != "3":
            print("{} {} ({}, {}): {} = {}, {} = {}, {} {}".format(
                var["fname"], var["lname"], var["gender"], var["age"], "Overall GPA",
                var["overall_gpa"], "Major GPA", var["major_gpa"],
                var["years_experience"], "Years Experience"))
        else:
            print("{} {} ({}, {}): {} = {}, {} = {}, {} {} ({} = {:.1f})".format(
                var["fname"], var["lname"], var["gender"], var["age"], "Overall GPA",
                var["overall_gpa"], "Major GPA", var["major_gpa"],
                var["years_experience"], "Years Experience", "Score", var["score"]))

def readCsv(filename):
    """
    This function creates a list of dictionaries for CSV data sets
    """
    ref = open(filename, "r")
    header = ref.readline().strip().split(",")
    lst = []
    cur = ref.readline()
    while cur != "":
        my_dict = {}
        row = cur.strip().split(",")
        for i in range(len(header)):
            my_dict[header[i]] = row[i]
        lst.append(my_dict)
        cur = ref.readline()
    ref.close()
    return lst

def sort(a_list, key):
    """
    This function is a bubble sort
    """
    # bubble sort – sort list in descending order (i.e. largest to smallest)
    for i in range(len(a_list) - 1):
        for j in range(i + 1, len(a_list)):
            if a_list[j][key] > a_list[i][key]:
                tmp = a_list[i]
                a_list[i] = a_list[j]
                a_list[j] = tmp
    return a_list

def filterOverallGpa(applicants, top_n):
    """
    Filters a CSV file with the bubble sort for overall GPA
    """
    for i in applicants:
        i["overall_gpa"] = float(i["overall_gpa"])
        i["advanced_gpa"] = float(i["advanced_gpa"])
        i["intro_gpa"] = float(i["intro_gpa"])
        i["intermediate_gpa"] = float(i["intermediate_gpa"])
        i["years_experience"] = int(i["years_experience"])
        adv = 10 * i["advanced_gpa"]
        inter = 8 * i["intermediate_gpa"]
        intro = 6 * i["intro_gpa"]
        ovr = 4 * i["overall_gpa"]
        yrs = 0.25 * i["years_experience"]
        i["score"] = adv + inter + intro + ovr + yrs
    return sort(applicants, "overall_gpa")[:top_n]

def filterMajorGpa(applicants, top_n):
    """
    Filters a CSV file with the bubble sort for major GPA
    """
    for i in applicants:
        i["overall_gpa"] = float(i["overall_gpa"])
        i["advanced_gpa"] = float(i["advanced_gpa"])
        i["intro_gpa"] = float(i["intro_gpa"])
        i["intermediate_gpa"] = float(i["intermediate_gpa"])
        i["years_experience"] = int(i["years_experience"])
        adv = 10 * i["advanced_gpa"]
        inter = 8 * i["intermediate_gpa"]
        intro = 6 * i["intro_gpa"]
        ovr = 4 * i["overall_gpa"]
        yrs = 0.25 * i["years_experience"]
        i["score"] = adv + inter + intro + ovr + yrs
    return sort(applicants, "major_gpa")[:top_n]

def filterCustomScore(applicants, top_n):
    """
    Filters a CSV file with the bubble sort for a custom score
    """
    for i in applicants:
        i["overall_gpa"] = float(i["overall_gpa"])
        i["advanced_gpa"] = float(i["advanced_gpa"])
        i["intro_gpa"] = float(i["intro_gpa"])
        i["intermediate_gpa"] = float(i["intermediate_gpa"])
        i["years_experience"] = int(i["years_experience"])
        adv = 10 * i["advanced_gpa"]
        inter = 8 * i["intermediate_gpa"]
        intro = 6 * i["intro_gpa"]
        ovr = 4 * i["overall_gpa"]
        yrs = 0.25 * i["years_experience"]
        i["score"] = adv + inter + intro + ovr + yrs
    return sort(applicants, "score")[:top_n]

main()
