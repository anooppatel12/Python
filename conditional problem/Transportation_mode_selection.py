#Choose a mode of transportaion based on the distance(e.g, <3 km: Walk, 3-15 km: Bike, >15 km: car).

distance = 5

if distance <3:
    transport = "Walk"
elif distance <=15:
    transport = "Bike"
else:
    transport = "Car"

print(transport)
