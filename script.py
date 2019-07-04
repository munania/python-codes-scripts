from statistics import mean as m

admins = {"python":"python123"}

studentDict = {"Jeff":[87,56,84],
               "Mark":[57,56,75],
               "Dan":[73,77,92]}

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,"Has an average grade of ",avgGrade)

def removeStudent():
    nameToRemove = input("What student to remove?: ")
    if nameToRemove in studentDict:
        print("Removing student...")
        del studentDict[nameToRemove]


def enterGrades():


    nameToEnter = input("Student Name: ")

    GradeToEnter = input("Grade: ")

    if nameToEnter in studentDict:

        print("Adding Grade...")

        studentDict[nameToEnter].append(int(GradeToEnter))

    else:

        print("Student does not exist.")

    print(studentDict)

def main():

    print('''
    What do you want to do today ?
    [ 1 ] - Enter Grades
    [ 2 ] - Remove Student
    [ 3 ] - Students Average Grades
    [ 4 ] - Exit
    ''')
    action = input('Choose an option from the list above (use the numbers): ')

    if action == "1":
        enterGrades()
    elif action == "2":
        removeStudent()
    elif action == "3":
        studentAVGs()
    elif action == "4":
        exit()
    else:
        print("Choose an appropriate option")

login = input("Username: ")

passw = input("Password: ")

if login in admins:
    if admins[login] == passw:
        print("welcome,",login)
        while True:
              main()
    else:
        print("Invalid password will detonate in 5 seconds")

else:
    print("Invalid choice given calling the FBI")
