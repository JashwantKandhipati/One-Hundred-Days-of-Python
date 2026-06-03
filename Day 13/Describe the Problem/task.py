def my_function():
    for i in range(1, 21):  # was 20, but changed to 21
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
        # go through the numbers 1-20
# 2. When is the function meant to print "You got it"?
        # when i == 20 print "You got it"
# 3. What are your assumptions about the value of i?
        # i never actually reaches 20, as 20 is the stop value
