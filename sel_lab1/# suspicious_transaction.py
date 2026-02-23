# Taking transaction amount input from user
amount = float(input("Enter transaction amount: "))

# Taking account age in months
account_age = int(input("Enter account age in months: "))

# Checking whether transaction is international
international = input("Is the transaction international? (yes/no): ").lower()

# Applying selection statement with AND condition
if amount > 200000 and account_age < 6 and international == "yes":
    print("⚠ Transaction flagged for manual verification.")
else:
    print("Transaction is normal.")