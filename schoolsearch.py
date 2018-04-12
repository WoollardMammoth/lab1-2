
# Schoolsearch Program: Meant to parse a file of students named "students.txt" and retrieve
#  various bits of data about a student based on input

# Authors: Griffin Cloonan, Nick Ponce, and Landon Woollard
# Date: April 6, 2018

import sys

# Print statement for testing
def print2(s):
   if(len(sys.argv) > 1 and sys.argv[1] == "-t"):
      return
   else:
      print s,

# Takes a criteria and a search type (0-7) and returns a list of strings representing students
# type:
# Old Format:
#     0           1           2        3     4     5     6           7
# StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName

# New Format:
#     0           1           2        3     4     5 
# StLastName, StFirstName, Grade, Classroom, Bus, GPA
# and
#     0           1          2
# TLastName, TFirstName, Classroom

def queryStudentsByCriteria(criteria, search_type):
   try:
      list_file = open("list.txt", "r")
   except:
      print("Error opening list file")
      exit()

   criteria = criteria.upper()

   studentList = []
   for student in list_file:
      student = student[:-2]
      studentData = student.split(",")
      teacherData = queryTeacherByCriteria(studentData[3], 2) # Will always return a valid classroom if input files are valid
      studentData.append(teacherData[0])
      studentData.append(teacherData[1])
      if studentData[search_type] == criteria:
         studentData[1] = studentData[1][+1:]
         studentList.append(",".join(studentData))
   return studentList

def queryTeacherByCriteria(criteria, search_type):
   try:
      teacher_file = open("teachers.txt", "r")
   except:
      print("Error opening teacher file")
      exit()

   criteria = criteria.upper()

   teacherData = []
   for teacher in teacher_file:
      teacherData = teacher.split(",")
      teacherData[1] = teacherData[1][+1:]
      teacherData[2] = teacherData[2][+1:-2]
      if(teacherData[search_type] == criteria):
         return teacherData
   return []         

# Takes an array of student data strings and prints the student's name, grade, classroom, and teacher
def printStudentDataByName(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print("Student: " + studentData[1] + " " + studentData[0] + "\nGrade: " + studentData[2] + "\nClassroom: " + studentData[3] + "\nTeacher: " + studentData[7] + " " + studentData[6])

# Takes an array of student data strings and prints the student's name and bus route
def printStudentBusData(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print "Student: " + studentData[1] + " " + studentData[0] + "\nBus Route: " + studentData[4]

# Takes an array of student data strings and prints the student's name
def printStudents(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print "Student: " + studentData[1] + " " + studentData[0]

# Takes an array of student data strings and prints the student's name
def printStudentsByBus(studentQuery):
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      print "Student: " + studentData[1] + " " + studentData[0] + "\nGrade: " + studentData[2] + "\nClassroom: " + studentData[3]

# Takes an array of student data strings, calculates the student with the highest gpa and prints their name, gpa, teacher, and bus route
def printHighestGPAStudent(studentQuery):
   highestGPAStudent = studentQuery[0].split(",")
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      if(float(studentData[5]) > float(highestGPAStudent[5])):
         highestGPAStudent = studentData
   print "Highest GPA Student: " + highestGPAStudent[1] + " " + highestGPAStudent[0] + "\nGPA: " + highestGPAStudent[5] + "\nTeacher: " + highestGPAStudent[7] + " " + highestGPAStudent[6] + "\nBus Route: " + highestGPAStudent[4]

# Takes an array of student data strings, calculates the student with the lowest gpa and prints their name, gpa, teacher, and bus route
def printLowestGPAStudent(studentQuery):
   lowestGPAStudent = studentQuery[0].split(",")
   for s in range(0, len(studentQuery)):
      studentData = studentQuery[s].split(",")
      if(float(studentData[5]) < float(lowestGPAStudent[5])):
         lowestGPAStudent = studentData
   print "Lowest GPA Student: " + lowestGPAStudent[1] + " " + lowestGPAStudent[0] + "\nGPA: " + lowestGPAStudent[5] + "\nTeacher: " + lowestGPAStudent[7] + " " + lowestGPAStudent[6] + "\nBus Route: " + lowestGPAStudent[4]

# Takes an array of student data strings, calculates the average GPA for a grade and prints it out
def printAverageGPAForGrade(studentQuery, query):
   avgGPA = 0
   for s in range(0, len(studentQuery)):
      avgGPA += float(studentQuery[s].split(",")[5])
   if(len(studentQuery) > 0):
      print("Grade: %s\nAverage GPA: %.2f\n" % (studentQuery[0].split(",")[2], (avgGPA / len(studentQuery))))
   elif(len(studentQuery) == 0):
      print("Grade: %s\nAverage GPA: 0\n" % query)

# Prints the number of students in each grade level
def printStudentsPerGrade(studentsPerGrade):
   for grade in range(0, len(studentsPerGrade)):
      print("Grade %d: Students: %d\n" % (grade, studentsPerGrade[grade]))

def main():
   print2("Welcome to SchoolSearch")
   choice = ""
   name = ""
   dataQuery = ""
   studentsPerGrade = []
   while(choice.lower() != "q"):
      print2("\n\nEnter a letter to begin a search:\n")
      print2("   S[tudent]\n   T[eacher]\n   B[us]\n   G[rade]\n   A[verage]\n   I[nfo]\n   Q[uit]\n> ")
      try:
         choice = raw_input()
      except EOFError:
         return

      if(choice.lower() == "s"):
         print2("S[tudent]: <lastname> [B[us]]\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         name = parts[0].upper()
         dataQuery = queryStudentsByCriteria(name, 0);
         if(len(parts) == 1):
            printStudentDataByName(dataQuery)
            #Valid format
            #Call function to search name and print details + class
         elif(len(parts) == 2):
            if(parts[1].lower() == "b"):
               #valid format
               printStudentBusData(dataQuery)
               #Call function to search name and print details + bus
            else:
               print("Invalid query.")
         else:
            print("Invalid query.")

      if(choice.lower() == "t"):
         print2("T[eacher]: <lastname>\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         name = parts[0].upper()
         dataQuery = queryStudentsByCriteria(name, 6);
         if(len(parts) == 1 and len(dataQuery) > 0):
            printStudents(dataQuery)
         else:
            print("Invalid query.")
         #function to search teacher name


      if(choice.lower() == "b"):
         print2("B[us]: <number>\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         #function to search bus by number
         if(query.isdigit()):
            dataQuery = queryStudentsByCriteria(query, 4)
            printStudentsByBus(dataQuery)
         else:
            print("Invalid query.")

      if(choice.lower() == "g"):
         print2("G[rade]: <number> [H[igh]|L[ow]]\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         parts = query.split()
         if(len(parts) > 2):
            print("Invalid query.")
         elif(len(parts) == 2):
            #first entry is a number, check for valid H or L flags
            dataQuery = queryStudentsByCriteria(parts[0], 2)
            if(parts[1].lower() == "h"):
               printHighestGPAStudent(dataQuery)
            elif(parts[1].lower() == "l"):
               printLowestGPAStudent(dataQuery)
            else:
               print("Invalid query.")
         else:
            #First entry is a number, no flags present
            dataQuery = queryStudentsByCriteria(parts[0], 2)
            printStudents(dataQuery)


      if(choice.lower() == "a"):
         print2("A[verage]: <number>\n> ")
         try:
            query = raw_input()
         except EOFError:
            return
         #function to search GPA average by grade
         if(query.isdigit()):
            dataQuery = queryStudentsByCriteria(query, 2)
            printAverageGPAForGrade(dataQuery, query)
         else:
            print("Invalid query.")


      if(choice.lower() == "i"):
         #function for grade by grade breakdown
         print2("I[nfo]")
         for grade in range(0, 7):
            dataQuery = queryStudentsByCriteria(str(grade), 2)
            studentsPerGrade.append(len(dataQuery))
         printStudentsPerGrade(studentsPerGrade)

   print2("Goodbye!")

if __name__ == "__main__":
    main()
