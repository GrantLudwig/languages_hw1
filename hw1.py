
import sys

#returns a list in the following format:
#   [[(student ID, first name, last name), 
#   [(department, number, credits, letter grade),(another class), ...)]], 
#   [another student info], ...]
def processFile(fileName):
    list = []
    for line in open(fileName):
        line = line.rstrip()
        stuLine = line.split()
        stuTuple = (int(stuLine[0]), stuLine[1], stuLine[2])
        stuList = [stuTuple]
        classList = []
        #generates a class tuple as such:
            #(department, number, credits, letter grade)
        #adds to the classList
        for i in range(0, int(stuLine[3])):
            classtuple = (stuLine[4 + 4*i], int(stuLine[5 + 4*i]), int(stuLine[6 + 4*i]), stuLine[7 + 4*i])
            classList.append(classtuple)
        stuList.append(classList)
        list.append(stuList)
    return list

def getGrade(letter):
    if letter == "A":
        return 4.0
    elif letter == "A-":
        return 3.7
    elif letter == "B+":
        return 3.3
    elif letter == "B":
        return 3.0
    elif letter == "B-":
        return 2.7
    elif letter == "C+":
        return 2.3
    elif letter == "C":
        return 2.0
    elif letter == "C-":
        return 1.7
    elif letter == "D+":
        return 1.3
    elif letter == "D":
        return 1.0
    elif letter == "D-":
        return 0.7
    else:
        return 0.0

def createStudentDict(list):
    dict = {}
    for student in list:
        totalGp = 0.0
        numCreds = 0
        for tuple in student[1]:
            numCreds += tuple[2]
            totalGp += getGrade(tuple[3]) * tuple[2]
        if numCreds == 0:
            dict[student[0][0]] = 0.0
        else:
            dict[student[0][0]] = totalGp / numCreds
    return dict

def createRoster(list, dep, classNum):
    returnList = []
    for student in list:
        for tuple in student[1]:
            if dep == tuple[0] and classNum == tuple[1]:
                studInfo = (student[0][0], student[0][1], student[0][2], tuple[3])
                returnList.append(studInfo)
    return returnList

def createCourseSet(list):
    courseSet = set()
    for student in list:
        for tuple in student[1]:
            courseSet.add(tuple[0] + " " + str(tuple[1]))
    return courseSet

def printStudents(list):
    dict = createStudentDict(list)
    list = sorted(list)
    for student in list:
        output = ""
        #goes through the student's info tuple
        for studInfo in student[0]:
            output += str(studInfo) + " "
        output += str(dict[student[0][0]])
        print(output)

   
#driver code
fileName = sys.argv[1]
studentList = processFile(fileName)
print("\n")
print(studentList)
print("\n")
dict = createStudentDict(studentList)
print(dict)
print("\n")
CPSClist = createRoster(studentList, "CPSC", 1420)
print(CPSClist)
print("\n")
mathList = createRoster(studentList, "Math", 2340)
print(mathList)
print("\n")
set = createCourseSet(studentList)
print(set)
print("\n")
printStudents(studentList)