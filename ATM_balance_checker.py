print("--------------------------Welcome to Sudarshan Bank ATM--------------------------")
print("Please insert your ATM card")
pin="1234"
#enter the pin
pin_input=input("Please enter your ATM pin:     ")
#check if the pin is correct
if pin_input== pin:
    min_balance=1000
    balance=10000
    print("Pin is correct")
    print("You can access your account")
#display the options
    while True:
        print("1.Check Balance")
        print("2.Withdraw Money")
        print("3.Transfer Money")
        print("4.Deposit Money")
        print("5.Exit")
        #enter the choice
        choice=int(input("Enter your choice:"))
        if choice==1:
        #check the balance
            print(f"your current balance is Rs: {balance}  ")
        elif choice==2:
        #withdraw money
            withdraw_amount=float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= balance:
                #check if the withdrawal is less thanbalance
                if balance>min_balance:
                    #check if the balnce is less than minimum balance
                    print(f"Please collect your cash: Rs {withdraw_amount}")
                    balance-=withdraw_amount
                    print(f"Your new balance is Rs {balance}")
                else:
                    print("Insufficient balance")
                    print(f"Minimum balance required is Rs {min_balance}")
            else:
                print("Insufficient balance")
                print(f"Minimum withdrawal amount is Rs {min_balance}")
        elif choice==3:
            transfer_amount=float(input("Enter the amount to transfer: "))
            if transfer_amount <= balance:
                if balance>min_balance:
                    print(f"Please collect your cash: Rs {transfer_amount}")
                    balance-=transfer_amount
                    print(f"Your new balance is Rs {balance}")
                else:
                    print("Insufficient balance")
                    print(f"Minimum balance required is Rs {min_balance}")
            else:
                print("Insufficient balance")
                print(f"Minimum transfer amount is Rs {min_balance}")
        elif choice==4:
            deposit_amount=float(input("Enter the amount to deposit: "))
            balance+=deposit_amount
            print(f"Your new balance is Rs {balance}")
        elif choice==5:
            print("Thank you for using Sudarshan Bank ATM")
            break
        else:
            print("Invalid choice")
else:
    print("Incorrect PIN. Please try again.")
