print("Welcome to three digit PIN cracker v2\n")
correct_password="042"
for i in range(0,1000):
    guss=str(i).zfill(3)
    print("Trying PIN:", guss)
    if guss==correct_password:
        print(f"Cracked PIN is : {guss}")
        break