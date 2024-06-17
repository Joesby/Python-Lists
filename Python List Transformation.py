#Task 1: Sort the following list in descending order
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#sort the list in ASCENDING order
grades.sort()
#then reverse it so it is DESCENDING, then display the list
grades.reverse()
print(grades)

#Task 2: Calculate the average grade and display it

#create a variable based on the number of elements in the grades list
number_of_elements = len(grades)
#create a variable to store our finalized average value
average = 0
#create a loop to cycle enough times to go through every item in the element
while number_of_elements != 0:
    #while cycling through the loop, add up the sum of all of the grades
    #start with number_of_elements minus one to stay within the boundaries of the list
    average = average + grades[number_of_elements - 1]
    #determine if the current grade in the loop is less than 80, if it is replace the element with "Failed"
    if grades[number_of_elements - 1] < 80:
        grades[number_of_elements - 1] = "Failed"

    number_of_elements -= 1

#reset the number of elements after iterating through the loop
number_of_elements = len(grades)
#once the loop ends and we have the sum of the grades, divide the sum by the number of elements to get the finalized average
average = average / number_of_elements

print("Average grade: " + str(average))

#Task 3: Replace any grade below 80 with the value "Failed"
#used the loop coded in Task 2 for efficiency
print(grades)