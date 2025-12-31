text = input("Enter message: ")
shift = int(input("Enter shift number: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

text = text.upper()

for char in text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = (position + shift) % 26
        result += alphabet[new_position]
    else:
        result += char

print("Encrypted text:", result)

