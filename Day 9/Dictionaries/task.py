programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# how to print a value from a dictionary.

# print(programming_dictionary["Bug"])

# How to add another entry
programming_dictionary["Loop"] = "The action of doing something over and over again"

# edit an item in the dictionary
programming_dictionary["Bug"] = "The loop is now changed"
print(programming_dictionary)

# empty dictionary
empty_one = {}

# erase all contents of existing dictionary
    # programming_dictionary = {}

# Looping through a dictionary and print the keys
for key in programming_dictionary:
    print(key)

# looping through a dictionary and printing the values
for key in programming_dictionary:
    print(programming_dictionary[key])