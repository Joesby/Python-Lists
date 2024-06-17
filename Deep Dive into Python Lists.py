students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

students_approved = []

#Tast 1: Filter out students who have grades below 80. Print the name, grade and activiy.
#iterate through the grades list, checking if each element is less than 80
for i in grades:
    if i < 80:
        #if a grade is less than 80, find the index number of the current element and print from the same location in other lists
        print(students[grades.index(i)] + ", " + str(i) + ", " + activities[grades.index(i)])
    
    #Task 2: For the remaining students, add students name in a new list named students_approved
    #using the index of the current element, add the student with the same index number to the new list
    else:
        students_approved.append(students[grades.index(i)])

#Task 3: Print the list students_approved
print(students_approved)