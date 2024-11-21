# A calculator to find the total of the bill plus tip.
# Then split the bill equally based on the amount of people.

# Print a welcome message for the user
print("Welcome to the tip calculator")

# Prompt the user to input the total bill amount and convert it to a float
bill_total = float(input("What was the total bill? $"))

# Prompt the user to input the desired tip percentage and convert it to a float
tip = float(input("How much tip would you like to tip?\n"))

# Convert the tip percentage into a decimal (e.g., 15% -> 0.15)
tip_conversion = tip / 100

# Prompt the user to input the number of people to split the bill and convert it to an integer
total_people = int(input("How many people to split the bill?\n"))

# Calculate the total tip amount by multiplying the bill total by the tip percentage
bill_tip = bill_total * tip_conversion

# Calculate the total bill by adding the original bill amount and the tip amount
total_bill = bill_total + bill_tip

# Calculate how much each person should pay by dividing the total bill by the number of people
person_pay = (total_bill / total_people)

# Round the amount each person pays to 2 decimal places
round_num = round(person_pay, 2)

# Format the rounded amount as a string to always display two decimal places
round_num = "{:.2f}".format(round_num)

# Print the final amount each person should pay
print(f"Each person should pay: ${round_num}")
