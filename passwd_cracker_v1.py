print("Welcome to number PIN cracker v1")
correct_password="7"
for guss in range(1,10):
    print(f"Trying PIN: {guss}")
    if str(guss) == correct_password:
        print(f"Cracked PIN is {guss}")
        break