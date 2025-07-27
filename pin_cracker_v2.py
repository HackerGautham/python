print("Welcome to two digit PIN cracker v2\n")
correct_password="42"
for i in range(1,100):
    guss=str(i).zfill(2)
    print("Trying PIN:", guss)
    if guss==correct_password:
        print(f"Cracked PIN is : {guss}")
        break