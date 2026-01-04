user_number = int(input("Please enter a number: "))

even_odd = user_number % 2

if even_odd == 0:
    print(f"The number {user_number} is even")
else:
    print(f"the number {user_number} is odd")