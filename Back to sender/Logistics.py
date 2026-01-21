print("""
    Collection Rate    Amount per Parcel     Base Pay

     less than 50%         160                5000
      50% - 59%            200                5000
      60% - 69%            250                5000
      >= 70%               500                5000
""")

rider_name = input("Enter rider's name: ")
collection_rate = int(input("Enter collection rate (%): "))
deliveries = int(input("Enter number of successful deliveries: "))

base_pay = 5000

if collection_rate < 50:
    amount_per_parcel = 160
elif collection_rate <= 59:
    amount_per_parcel = 200
elif collection_rate <= 69:
    amount_per_parcel = 250
else:
    amount_per_parcel = 500

wage = (deliveries * amount_per_parcel) + base_pay

print("Rider Name:", rider_name)
print("Rider Wage:", wage)

