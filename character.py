def character(word, number):
    result = ""

    for char in word: 
        result += char*number
    return result
word = input("enter word: ")
number = int(input("enter a number: "))

print(character(word, number))

