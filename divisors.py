num = int(input("Enter a number: "))


for count in range(1, num + 1):
    if num % count == 0:  
        print(count, end=" ")

