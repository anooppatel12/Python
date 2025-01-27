#Movie Tickets are priced basedon age: $12 for adults(18 and over), $8 for children. Everyone gets a 2$ discount on wednesday.

age = int(input("Enter Your age:"))
day = str(input("Enter day:"))

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price-2

print("Tickewt price for you is $", price)
