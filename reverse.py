text = input("Enter a string: ")

reversed_text = ""

for counter in range(len(text) - 1, -1, -1):
    reversed_text += text[counter]

print("Reversed string:", reversed_text)
