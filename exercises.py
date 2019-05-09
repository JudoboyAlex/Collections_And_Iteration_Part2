#Exercise9
# grocery_list = ["carrots", "toilet paper", "apples", "salmon"]
# Your next step should present your grocery list with an item on each line, with an asterisk (*) in front of it so that it appears like this:
# for item in grocery_list:
#     item = "*" + item
#     print(item)
# #You realize you've forgotten some rice, so add it to your list and output it again. Given that you've already output your list twice, it might be good to consider writing a method to do this. Putting frequently used chunks of code in a method lets you reuse them throughout your program without having to type them out over and over.
# grocery_list.append("apple")
# print(grocery_list)
# #You lost count of how many things you need to pick up. Better output the total number of items on your list.
# print(len(grocery_list))
# #Check to see if your list includes "bananas". If it does, output "You need to pick up bananas". Otherwise, output "You don't need to pick up bananas today".

# if grocery_list.count('bananas') > 0 :
#     print("You don't need to pick up bananas today")
# else:
#         print("You need to pick up bananas")
# It turns out that everything in this grocery store you're visiting is stored alphabetically, so to better plan out what you need to buy you should sort your grocery list and output it with asterisks again.
# grocery_list.sort()
# for item in grocery_list:
#     item = "*" + item
#     print(item)
# # After looking everywhere, you can't find the salmon. Delete it from your list and redisplay the list one last time.
# grocery_list.pop(2)
# print(grocery_list)

#Exercise10
#Start out by creating the following dictionary representing the number of students in past Bitmaker cohorts:
students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}
#Create a method that displays the name and number of students for each cohort, like so:
# for key, value in students.items():
#     print("{}: {} students".format(key, value))                         
# Add cohort 4, which had 43 students, to the dictionary.
students["cohorts4"] = 43
# print(students)
#Use the keys method to output all of the cohort names.
# print(students.keys())
#The classrooms have been expanded! Increase each cohort size by 5% and display the new results.
# for key in students:    
#     students[key] *=  1.05
# print(students)
# Delete the 2nd cohort and redisplay the dictionary.
students.pop("cohort2")
# print(students)
# BONUS: Calculate the total number of students across all cohorts using a for loop. Output the result.
# print(sum(students.values()))
total = 0
for key, value in students.items():
  total = total + value
print(total)


