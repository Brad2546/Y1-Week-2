if __name__ == "__main__":
    noOfStudents = int(input("Enter number of students? "))
    requiredGroupSize = int(input("Enter required group size? "))
    noOfGroups = noOfStudents // requiredGroupSize
    noLeftOver = noOfStudents % requiredGroupSize
    if noLeftOver == 1:
        studentsCorrectGrammar = "student"
    else:
        studentsCorrectGrammar = "students"
    print("There will be",noOfGroups,"groups with",noLeftOver,studentsCorrectGrammar,"left over")