text = input("Enter a string: ")
count = 0

for char in text:
    if char == 'e':
        count += 1

print("Number of 'e' characters:", count)
