#Check if a password is "Weak", "Medium", or "Strong". Criteria: <6 chars(weak), 6-10 chars(medium), >10 chars(Strong).

password = input("Check Your Password:")

if len(password) < 6:
    strength = "Weak"
elif len(password) <=10:
    strength = "Medium"
else:
    strength = "Strong"

print(strength)
    
    
