#Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79),D(60-69),F(below 60).

n = int(input("Enter Your Number:"))

if n >=101:
    print("Enter Vslid Number")
    exit()


if n >= 90:
    print("Grade A")
elif n>=80 :
    print("Grade B")
elif n >= 70:
    print("Grade C")
elif n >= 60:
    print("Grade D")
elif n<60:
    print("Fail")
else:
    print("Enter Correct Vslue")
