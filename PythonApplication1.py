
import sys

def processFile(fileName):
    list = []
    for line in open(fileName):
        line = line.rstrip()
        stuLine = line.split()
        stuTuple = (stuLine[0], stuLine[1], stuLine[2])
        stuList = [stuTuple]
        for i in range(0, int(stuLine[3])):
            classtuple = (stuLine[4 + 4*i], stuLine[5 + 4*i], stuLine[6 + 4*i], stuLine[7 + 4*i])
            stuList.append(classtuple)
        list.append(stuList)
    return list

def createStudentDict(list):
    dict = {}
    for student in list:
        totalGp = 0.0
        numCreds = 0
        for tuple in student:
            if len(tuple) == 4:
                numCreds += int(tuple[2])
                gp = 0.0
                if tuple[3] == "A":
                    gp = 4.0
                elif tuple[3] == "A-":
                    gp = 3.7
                elif tuple[3] == "B+":
                    gp = 3.3
                elif tuple[3] == "B":
                    gp = 3.0
                elif tuple[3] == "B-":
                    gp = 2.7
                elif tuple[3] == "C+":
                    gp = 2.3
                elif tuple[3] == "C":
                    gp = 2.0
                elif tuple[3] == "C-":
                    gp = 1.7
                elif tuple[3] == "D+":
                    gp = 1.3
                elif tuple[3] == "D":
                    gp = 1.0
                elif tuple[3] == "D-":
                    gp = 0.7
                totalGp += gp * int(tuple[2])
        if numCreds == 0:
            dict[student[0][0]] = 0.0
        else:
            dict[student[0][0]] = totalGp / numCreds
    return dict

        
#driver code
fileName = sys.argv[1]
studentList = processFile(fileName)
print(studentList)
dict = createStudentDict(studentList)
print(dict)
