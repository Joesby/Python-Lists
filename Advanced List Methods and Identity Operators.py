submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

#Task 1: Find out which students both submitted their assignments and attended the class
#create a variable to iterate through a loop and set it to the length of the attended list
iterator = len(attended)
identical = True

#loop through all of submitted list, checking for each element in attended list, output names that are in both
while iterator != 0:
    if attended[iterator -1] in submitted:
        print(attended[iterator -1] + " submitted their assignment and attended class.")
        iterator -= 1
    
    #Task 2: Check if the two lists are identical in terms of their content, regardless of order
    #using the identical variable, check if the current element in the loop is NOT in the attended list, and if not
    #make identical false
    elif attended[iterator -1] not in submitted:
        identical = False
        #Task 3: Using list methods, remove any student from the attended list who did not submit their assignment
        #remove any element in the attended list if they aren't in the submitted list
        attended.remove(attended[iterator -1])
        iterator -= 1

#once the loop has been completed, print whether or not the lists are the same
if identical == False:
    print("These lists are not identical.")
else:
    print("These lists are identical.")

#disply the lists after changes are made
print(submitted)
print(attended)