from banking_system import BankAccount, SavingsAccount

def main():
    print("=== BANK SIMULATION ===")

    # 1. Normal Account
    john = BankAccount("John Doe", 100)
    john.deposit(50)
    john.withdraw(20)
    john.print_statement()

    print("\n=== SAVINGS SIMULATION ===")

    # 2. Savings Account
    jane = SavingsAccount("Jane Doe", 1000)
    jane.deposit(500)
    jane.apply_interest() # Special method
    jane.print_statement()

if __name__ == "__main__":
    main()