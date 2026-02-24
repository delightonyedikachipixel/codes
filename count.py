word = input("Enter word: ")

vowels = 0
consonants = 0

for counter in range(len(word)):

    character = word[counter]

    
    if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):

        
        if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u' or
            character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):

            vowels += 1
        else:
            consonants += 1


print("The Number Of Vowels is", vowels)
print("The Number Of Consonants is", consonants)
