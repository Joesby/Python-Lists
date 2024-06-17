temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Task 1: Extract the temperatures for the second week (7 days) of the month
#create a variable to iterate through
iterator = 0
#create new list to store extracted tempuratures
week_two_temps = []
over_one_hundred = []
reversed_five_through_ten = []

#extract the tempurates of the second week to a new list
week_two_temps = temperatures[7:14]

#Task 2: Extract all the temperatures above 100
#iterate through the temperatures list, extracting any temperature over 100 to a new list
for i in temperatures:
    if i > 100:
        over_one_hundred.append(i)

#Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list
#reverse the temperatures list
temperatures.reverse()
#extract the tempuratures from the 5th to the 10th and store them in a new list
reversed_five_through_ten = temperatures[4:10]

print(week_two_temps)
print(over_one_hundred)
print(reversed_five_through_ten)