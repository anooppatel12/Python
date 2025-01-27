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
