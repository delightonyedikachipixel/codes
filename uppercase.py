
text = input("Enter a string: ")

uppercase_counter = 0


for ch in text:
    if 'A' <= ch <= 'Z':  
        uppercase_counter += 1

print("Number of uppercase letters:", uppercase_counter)
