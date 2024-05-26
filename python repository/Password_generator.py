import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]

number = ['1','2','3','4','5','6','7','8','9','0']

special = ['!','@','#','$','%','^','&','*','_','+']

in_letter = int(input("Please enter the number of letters for the password: "))
in_number = int(input("Please enter the number of digits you want in the password: "))
in_special = int(input("Please enter the number of special charachter you want in the password: "))
password_list = []

for char in range (1,in_letter+1):
    random_char = random.choice(letter)
    password_list += random_char 
for char in range (1,in_number+1):
    random_num = random.choice(number)
    password_list += random_num  
for char in range (1,in_special+1):
    random_sp = random.choice(special) 
    password_list += random_sp 

random.shuffle(password_list)


password = ""
for char in password_list:
    password+= char

print(password)    