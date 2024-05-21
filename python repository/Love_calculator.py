name1 = input("Please enter your name: ")
name2 = input("Please enter your lover name: ")

combined_name = name1 + name2

full_name = combined_name.lower()

t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')
first_digit = t+r+u+e

l = full_name.count('l')
o = full_name.count('o')
v = full_name.count('v')
e = full_name.count('e')
second_digit = l+o+v+e

total_score = int(str(first_digit) + str(second_digit))

if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
    print(f"Your score is {total_score}, you are alright together.")    
else:
    print(f"Your score is {total_score}.")
