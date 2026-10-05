# Create a Python ATM Machine Program that verifies a user's 4-digit PIN with a maximum of 3 attempts
# and temporarily blocks the card after three incorrect attempts.
# After successful login, allow the user to check balance,
# deposit cash, withdraw cash, change PIN, transfer funds to a 13-digit account,
# or safely exit the program, starting with a balance of Rs. 500,000.

pins = [1234, 5678, 9012]
balance = 500000
attempts = 0
logged_in = 0

# ---------- Login ----------
while attempts < 3:  # Allows a maximum of 3 PIN attempts
    user_pin = int(input("Enter PIN: "))

    if user_pin in pins:  # Checks if the entered PIN exists in the list
        print("Login Successful!")
        logged_in = 1  # Marks the user as successfully logged in
        break  # Stops the login loop after correct PIN
    else:
        print("Invalid PIN. Please try again.")
        attempts = attempts + 1  # Increases the wrong attempt count

if logged_in == 0:  # Checks if login was not successful
    print("Your Card is temporarily blocked due to multiple incorrect PIN attempts. Please contact your bank.")

# ---------- Menu ----------
while logged_in == 1:  # Shows the menu only after successful login
    print("\n========== Welcome to ATM Machine ==========")
    print("1. Balance Inquiry")
    print("2. Cash Deposit")
    print("3. Cash Withdrawal")
    print("4. PIN Change")
    print("5. Funds Transfer")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Current Balance is Rs.", balance)

    elif choice == "2":
        deposit = float(input("Enter the Amount to Deposit: Rs. "))
        balance = balance + deposit  # Adds the deposited amount to the balance
        print("Deposit Successful! Your New Balance is Rs.", balance)

    elif choice == "3":
        withdrawal = float(input("Enter the Amount to Withdraw: Rs. "))

        if withdrawal <= balance:  # Checks if enough balance is available
            balance = balance - withdrawal  # Deducts withdrawal amount from balance
            print("Withdrawal Successful! Your New Balance is Rs.", balance)
        else:
            print("Insufficient Balance for Withdrawal.")

    elif choice == "4":
        new_pin = int(input("Enter your New 4-digit PIN: "))

        if len(str(new_pin)) == 4:  # Checks whether the new PIN has exactly 4 digits
            pins.remove(user_pin)  # Removes the user's old PIN
            pins.append(new_pin)  # Adds the new PIN to the list
            user_pin = new_pin  # Updates the current PIN
            print("PIN Change Successful!")
        else:
            print("PIN must be 4 digits.")

    elif choice == "5":
        account = input("Enter the 13-digit Account Number: ")

        if len(account) == 13 and account.isdigit():  # Checks for exactly 13 numeric digits
            amount = float(input("Enter the Amount to Transfer: Rs. "))

            if amount <= balance:  # Checks if enough balance is available
                balance = balance - amount  # Deducts the transfer amount from balance
                print("Transfer Successful! Your New Balance is Rs.", balance)
            else:
                print("Insufficient Balance for Transfer.")
        else:
            print("Invalid account number.")

    elif choice == "6":
        print("Thank you for using the ATM Machine. Have a great day!")
        logged_in = 0  # Stops the menu loop and exits the ATM

    else:
        print("Invalid choice. Please enter 1 to 6.")