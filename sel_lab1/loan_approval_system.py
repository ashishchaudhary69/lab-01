

# Taking credit score input
credit_score = int(input("Enter credit score: "))

# Taking monthly income
income = float(input("Enter monthly income: "))

# Taking existing loan amount
existing_loan = float(input("Enter existing loan amount: "))

# Applying loan approval rules
if credit_score < 600:
    print("Loan Rejected: Credit score is too low.")

elif 600 <= credit_score < 750:
    # Further checking income and existing loan
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected: Low income and high existing loans.")
    else:
        print("Loan Approved after verification.")

else:  # credit_score >= 750
    print("Loan Approved: Excellent credit score.")