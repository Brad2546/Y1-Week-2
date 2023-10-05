if __name__ == "__main__":
    noOfStudents = int(input("Enter No of students: "))
    noOfSweets = int(input("Enter No of Sweets: "))
    noOfSweetsEach = noOfSweets // noOfStudents
    noOfSweetsLeft = noOfSweets % noOfStudents
    if noOfSweetsEach == 1:
        sweetsCorrectGrammar = "sweet"
    else:
        sweetsCorrectGrammar = "sweets"
    print("You should give each student",noOfSweetsEach,sweetsCorrectGrammar,"each, leaving",noOfSweetsLeft,"left over")