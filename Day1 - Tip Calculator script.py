print("Welcome to the Tip Calculator!")
total = float(input("What is the total bill? $ "))
tip = float(input("How much tip would you like to give? (in %) "))
people = int(input("How many people will share the bill? "))
bill_per_person = (total * (1 + tip / 100)) / people
print(f"Each person should pay: ${round(bill_per_person,2)}")
