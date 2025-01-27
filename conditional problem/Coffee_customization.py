#Customize a coffee order: "Small","Medium", or "Large" with an option for "Extrashot" of espresso.

order_size = "Medium"
extra_shot = True

if extra_shot:
    cofee = order_size + " Cofee with Extra Shot"
else:
    cofee = order_size+ " Cofee"

print("Order:", cofee)
