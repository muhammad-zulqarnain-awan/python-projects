print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split_bill = int(input("How many people to split the bill? "))

bill_per_person = round((total_bill + (total_bill * percent_tip / 100)) / split_bill, 2)

print(f"Each person should pay: ${bill_per_person}")