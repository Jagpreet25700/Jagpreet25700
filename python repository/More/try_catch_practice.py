"""try:
  file = open("a_file.txt")
  a_dictonary = {"key":"value"}
  print(a_dictonary["dsfaddg"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"{error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is the error that I made up")"""

height = float(input("Enter your height: "))
weight = int(input("Enter you weight: "))    

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight/height**2
print(bmi)

