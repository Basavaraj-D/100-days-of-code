print("Welcome to the tip calculator")

bill = float(input("what is the total bill ? $"))
tip = int(input("what percentage tip would you like to give ?10,12 or 15 : "))
people = int(input('how many people will split the bill ? :'))

total_tip = bill * tip/100
total_bill  = bill + total_tip
bill_per_person = round(total_bill / people,2)

print(f"Each person should pay ${bill_per_person}")

