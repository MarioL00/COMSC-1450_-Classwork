balance = int(input("Enter your starting balance: "))


def process_atm_transactions(balance):
    transaction_count = 0

    while True:
        amount = int(input("Enter transaction amount: "))
        if amount == 0:
            break
        elif amount > 0:
            balance += amount
            print(f"Deposited: {amount}. New balance: {balance}.")
            transaction_count += 1
        elif amount < 0: 
            if amount < -balance:
                print("Insufficient funds.")
            else:
                balance += amount
                print(f"Withdrew: {amount}. New balance: {balance}.")
                transaction_count += 1

    return balance,transaction_count

final_balance, total_successful_transactions = process_atm_transactions(balance)
print(f"Final Balance: {final_balance}.")
print(f"Total Successful Transactions: {total_successful_transactions}.")