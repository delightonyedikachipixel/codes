balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    match (choice):
        case 1:
            print("Your balance is:", balance)

        case 2:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit successful.")
            print("New balance:", balance)

        case 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
                print("New balance:", balance)
            else:
                print("Insufficient funds.")

        case 4:
            print("Thank you for using the ATM.")
            break

