text = input("Enter a string: ")
result = ""

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in text:
    for count in range(len(lowercase)):
        if char == lowercase[count]:
            result += uppercase[count]
            break
    else:
       
        result += char

print("Converted string:", result)
