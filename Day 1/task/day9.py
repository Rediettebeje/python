
# A dictionary in Python functions similarly to a dictionary in real life.
# It's a data structure that allows us to associate a key to a value
# and pair the two pieces of data together.


# An example dictionary
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

# This is how you retrieve items from a dictionary:

print(colours["pear"])
# #Will print "green"

# This is how to create an empty dictionary:
my_empty_dictionary = {}

# This is how you can add new items to an existing dictionary:
colours["peach"] = "pink"

# This is also how you can edit an existing value in a dictionary:
colours["apple"] = "green"

# This is how to loop through a dictionary and print all the keys:
for key in colours:
    print(key)

# This is how to loop through a dictionary and print all the values:
for key in colours:
    print(colours[key])

# a program that converts their scores to grades.
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)