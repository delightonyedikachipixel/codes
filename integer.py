number = input("Enter a string: ")

reversed_number = ""

for counter in range(len(number) - 1, -1, -1):
    reversed_number += number[counter]

print("Reversed Integer:", reversed_number)
