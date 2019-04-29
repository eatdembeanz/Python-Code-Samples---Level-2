#Benjamin Page
#4/23/2019

#https://stackoverflow.com/questions/27387415/how-would-i-get-everything-before-a-in-a-string-python
#Problem 4: Writes a program that calculates the average grade for each student, and prints out the student's name along with their average grade.



f = open("studentData.txt","r")
StudentTotals = {}
StudentAverages = {}
print(f)
for line in f:
    StudentName = line.split(':')[0]
    #print(StudentName)
    StudentScore = int(line.split(':')[2])
    #print(StudentScore)
    if StudentName not in StudentTotals:
        #print(StudentName)
        StudentAverage = StudentScore
        Occurrences = 1
        StudentTotals[StudentName] = [StudentScore,Occurrences]
        StudentAverages[StudentName] = [StudentAverage,Occurrences]

    else:
##        StudentScore += StudentScore
##        StudentTotals[Occurrences] += 1
        #print(StudentName)
        StudentTotals[StudentName] += [StudentScore, 1]
        StudentAverage = StudentScore / Occurrences
        StudentAverages[StudentName] = StudentAverage
        

print(StudentTotals)
print(StudentAverages)

        
f.close()
