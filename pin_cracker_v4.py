print("Welcome to four digit PIN cracker v2\n")
correct_password="2242"
for i in range(0,10000):
    guss=str(i).zfill(4)
    print("Trying PIN:", guss)
    if guss==correct_password:
        print(f"Cracked PIN is : {guss}")
        break