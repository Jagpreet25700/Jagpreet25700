#number = int(input())
number = [[1, 2], [3, 4], [5, 6]]  # Example input

result = []  # Use a different name to avoid confusion with the built-in `list`

for n in number:
    result += n  # Concatenate lists

print(result)

"""square = number **0.5

if square **2  == number:
    print(f"{number} is perfect square of {square} ")
else:
    print(f"{number} is not perfect square of {square} ")
"""

"""fact = 1
for n in range(1,number + 1):
    fact = fact*  n
print(fact)"""


def find_missing(input_list):
    sum_of_element = sum(input_list)
    print(sum_of_element)
    number = len(input_list) + 1
    print(number)
    actual_sum = int(number * (number + 1) /2)
    print(actual_sum)
    return (sum_of_element - actual_sum)



find_missing([1,2,4,5,6])