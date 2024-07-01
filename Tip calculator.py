# A calculator to find the total of the bill plus tip.
# Then split the bill equally based on the amount of people.

print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to tip?\n"))
tip_conversion = tip / 100
total_people = int(input("How many people to split the bill?\n"))
bill_tip = bill_total * tip_conversion
total_bill = bill_total + bill_tip
person_pay = (total_bill / total_people)
round_num = round(person_pay, 2)
round_num = "{:.2f}".format(round_num)
print(f"Each person should pay: ${round_num}")
