loan_amount = float(input("Enter loan amount: "))
years = float(input("Enter the loan duration (years): "))

total_months = years * 12
rate = 5.0



while rate <= 10.0:
    monthly_rate = rate / 100 / 12

    monthly_payment = (loan_amount * monthly_rate) / \
        (1 - (1 + monthly_rate) ** (-total_months))

    total_payment = monthly_payment * total_months

    print(f"{rate:.2f}%\t{monthly_payment:.2f}\t{total_payment:.2f}")

    rate += 0.25




