def show_balance(balance):
    print("---------------")
    print(f"Your current balance is: {balance:.2f}$")
    print("---------------")


def deposit(balance):
    amount = float(input("Please enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount!")
        return balance
    return balance + amount


def withdraw(balance):
    amount = float(input("Please enter an amount to be withdrawed: "))

    if amount > balance:
        print(f"Not enough balance! Your balance is: {balance}$")
        return balance
    elif amount <= 0:
        print("Amount must be greater than 0")
        return balance
    return balance - amount


def main():
    balance = 0.00
    is_running = True

    while is_running:
        print("======ATM======")
        print("1-Show Balance")
        print("2-Deposit")
        print("3-Withdraw")
        print("4-Exit")
        print("===============")
        choice = input("Enter your choice(1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance = deposit(balance)
            case "3":
                balance = withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("Wrong input!")

    print("Thanks, have a nice day!")


if __name__ == "__main__":
    main()
