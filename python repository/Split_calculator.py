print("Welcome to the tp calculator!")

total_bill = float(input("Please enter your total bill amount. "))
tip = float(input("How much tip that you would like to give? 10% , 12%, 15% "))
no_of_people = int(input("Please enter the total number of people you would like to slip the bill in. "))

tip_amount = (total_bill * tip)/100
split_amount = str((total_bill + tip_amount)/no_of_people)

print("You have to pay: " + split_amount)

