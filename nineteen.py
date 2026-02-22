number = input("Enter a number: ")
largest = 0

for digit in number:
    if int(digit) > largest:
        largest = int(digit)

print("Largest digit:", largest)
