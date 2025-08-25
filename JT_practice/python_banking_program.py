# Python Banking Program
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: $"))

    if amount < 0:
        print("Deposit amount must be positive.")
        return 0
    else:
        return amount
         
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Withdrawal amount must be positive.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*************************************")
        print("Welcome to the Python Banking Program")
        print("*************************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Thank you for using the Python Banking Program.")
        else:
            print(f"{choice} is not a valid option. Please choose a number between 1 and 4.")

    print("Thank you! Have a great day! 😊")

if __name__ == "__main__":
    main()