print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
tip = input("How much tip wou you like to give? 10, 12, or 15? ")
split = input("How many peoplle to split the bill? ")


n_bill = float(bill)
n_tip = int(tip)/100
n_split = int(split)

total = (n_bill + (n_bill * n_tip))/n_split

n_total = round(total, 2)

print(f"Each person should pay: $ {n_total}")
