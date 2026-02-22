
word = input("Enter a string: ")

position = 0


for count in range(len(word)):
    c = word[count]  
    if c in 'aeiouAEIOU':  
        position = count
        print(f"First vowel '{word[position]}' found at position: {position}")
       
