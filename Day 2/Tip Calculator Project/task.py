print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_of_bill = bill * (tip/100)
total_bill = bill + tip_of_bill
split_bill = total_bill / people
final_bill = round(split_bill, 2)
print(f"Each person should pay: ${final_bill}")

