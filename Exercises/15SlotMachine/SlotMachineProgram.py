import random


def spin_row():
    symbols = ["🍉", "🍋", "🍊", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    for item in row:
        print(item, end=" ")
    print()


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍉":
                return bet * 2
            case "🍋":
                return bet * 3
            case "🍊":
                return bet * 5
            case "🔔":
                return bet * 10
            case "⭐":
                return bet * 50
    return 0


def main():
    balance = 100
    print("=======================")
    print("Welcome to Slot Machine")
    print("=======================")

    while balance > 0:
        print(f"Current balance: {balance}$")
        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...")

        print_row(row)

        profit = get_payout(row, bet)
        if profit > 0:
            print(f"You won {profit}$")
        else:
            print(f"You lose this round")
        balance += profit

        choice = input("Do you want to continue?(Y/N): ").upper()
        if choice != "Y":
            break
    print("=======================")
    print(f"Game is over! Your current balance is {balance}$")
    print("=======================")


if __name__ == "__main__":
    main()
