correct_pin = "1234"
balance = 10000
attempts = 3
transactions = []

# Stage 1: PIN Check
while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN accepted.")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("Wrong PIN. Attempts left:", attempts)
        else:
            print("Card blocked.")

if attempts > 0:

    # Stage 2: Menu
    while True:
        print("\n--- ATM MENU ---")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current balance:", balance)

        elif choice == "2":
            # Stage 3: Deposit
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                transactions.append(f"Deposit {amount:g}")
                print("New balance:", balance)
            else:
                print("Amount must be above 0.")

        elif choice == "3":
            # Stage 3: Withdraw
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be above 0.")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                transactions.append(f"Withdraw {amount:g}")
                print("New balance:", balance)

        elif choice == "4":
            print("Thank you!")

            # Stage 4: Transaction History
            print("\nTransaction History:")

            for transaction in transactions:
                print(transaction)

            break

        else:
            print("Invalid choice. Try again.")