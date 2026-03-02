number = int(input("Enter a number: "))


if number <= 1:
    print(f"{number} is not prime")
else:
    is_prime = True
    for divider in range(2, number):
        if number % divider == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")


print(f"Prime numbers from 2 to {number} are:")

for number_inputed in range(2, number + 1):
    is_prime = True
    for divider in range(2, number_inputed):
        if number_inputed % divider == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number_inputed} is prime")
    else:
        print(f"{number_inputed} is not prime")

