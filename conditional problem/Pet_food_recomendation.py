#Recommend a type of pet food based on the pet's species and age.(e.g., Dog:<2 years - puppy food , CAt:>5 years - Senior cat food.)

pet = "Dog"
age = 2


if pet == "Dog":
    if age <2:
        food = "Puppy Food"
    else:
        food = "Normal Food"
elif pet == "Cat":
    if age >5:
        food = "Senior cat food"
    else:
        food = "baby cat food"

print(food)
