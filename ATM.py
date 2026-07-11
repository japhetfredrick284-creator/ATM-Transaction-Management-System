#intial Data
pin = "1234"
balance = 5000
min_statement = []

#function for chebking pin
def authenticate():
    entered_pin = input("\nEnter your pin: ")
    if entered_pin == pin:
        print("Login Successful: ")
        return True
    else:
        print("Incomplete Pin")
        return False

#Main ATM statement
def atm_statement():
    global balance, pin, min_statement
    while True:
        print("\n============== ATM MENU ===================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Mini Statement")
        print("6. Exit")
        print("="*44)

        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"Current Balance: ${balance}")
            min_statement.append(f"Checked Balance: ${balance}")

        elif choice == "2":
            amount = float(input("Enter Depoit Amount: $"))
            if amount > 0:
                balance += amount
                print(f"${amount} Deposit Saccessfully")
                print(f"Updatede Balance: ${balance}")
                min_statement.append(f"Deposit: ${amount}")
            else:
                print("Invalid Amount")

        elif choice == "3":
            amount = float(input(f"Enter Withdaw Amount: $"))
            if amount <= balance:
                if amount > 0:
                    balance -= amount
                    print(f"${amount} Withdaw Successfully")
                    print(f"Remaining Balance: ${balance}")
                    min_statement.append(f"Withdaw: ${amount}")
                else:
                    print("Invalid Amount")
            else:
                print("Insufficient Balance")

        elif choice == "4":
            old_pin = input("Enter Old Pin: ")
            if old_pin == pin:
                new_pin = input("Enter New Pin: ")
                confirm_pin = input("Confirm New Pin: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("Pin Changed Successfully")
                    min_statement.append(f"Pin Changed")
                else:
                    print("Pin Mismatch")
            else:
                print("Wrong Old Pin")

        elif choice == "5":
            print("\n------ MINI STATEMENT ---------")
            if len(min_statement) == 0:
                print("No Transactions Yet")
            else:
                for t in min_statement:
                    print("->", t)

        elif choice == "6":
            print("Thank you For Using ATM")
            print("Exiting System...")
            break
        else:
            print("Invalid Choice")

#Program Start
if authenticate():
    atm_statement()
else:
    print('Access Denied')
