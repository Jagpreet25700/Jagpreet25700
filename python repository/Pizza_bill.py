size = input("Hello and welcome to the PIZZA PLEX. To continue, please select the size. Type 'L' for Large,'M' for Medium and 'S' for Small:  ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20    
else:
    bill = 25

add_pepperoni = input("Do you want to add pepperoni? Press 'Y' for Yes or 'N' for No: ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3 
else:
    bill
add_cheese = input("Do you want to add cheese? Press 'Y' for Yes and 'N' for No: ")
if add_cheese == "Y":
    bill += 1
else:
    bill

print(f"Thanks for ordering the pizza. Your total bill is {bill}")    