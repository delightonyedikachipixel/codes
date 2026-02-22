text = input("Enter a string: ")

lowercase_counter = 0


for ch in text:
    if 'a' <= ch <= 'z':  
        lowercase_counter += 1

print("Number of lowercase letters:", lowercase_counter)
