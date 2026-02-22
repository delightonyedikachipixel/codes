num = int(input("Enter a number: "))

counter = 0
for count in range(1, num + 1):
    if num % count == 0:  
        counter +=1 
print(counter)

