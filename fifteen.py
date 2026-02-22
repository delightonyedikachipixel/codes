text = input("Enter a string: ")
result = ""

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

for char in text:
    for count in range(len(uppercase)):
        if char == uppercase[count]:
            result += lowercase[count]
            break
    else:
        result += char

print("Converted string:", result)
