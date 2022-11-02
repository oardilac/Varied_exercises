age = int(input("\nWrite your age: \n"))

if age > 122:
    age = str(age)
    print(f"You are {age} years old, that is, you are of LEGAL age, in fact, you hold the record for the longest-lived person in the world (you surpassed Jeanne Louise Calment).")

elif age > 17:
    age = str(age)
    print(f"You are {age} years old, that is, you are of LEGAL age.")

elif age < 0:
    age = str(age)
    print(f"You are {age} years old, that is, you weren't born.")

else:
    age = str(age)
    print(f"You are {age} years old, that is, you are UNDER age.")
