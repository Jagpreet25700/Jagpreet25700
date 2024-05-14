print("Welcome to the BMI Calculator.")
Weight = float(input("Please enter your weight (in Kilograms): "))
Height = float(input("Please enter your height (in meters)"))

BMI = str(Weight/(Height * Height))

print("Your BMI is " + BMI)