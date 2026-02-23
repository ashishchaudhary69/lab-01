
# Taking annual income input
income = float(input("Enter annual income: "))

# Taking age input
age = int(input("Enter age: "))

# Setting exemption limit based on age
if age >= 60:
    exemption = 300000   # Senior citizen exemption
else:
    exemption = 250000   # Normal exemption

# Initialize tax variable
tax = 0

# Applying income tax slabs
if income <= exemption:
    tax = 0

elif income <= 500000:
    tax = (income - exemption) * 0.05

elif income <= 1000000:
    tax = ((500000 - exemption) * 0.05) + ((income - 500000) * 0.20)

else:
    tax = ((500000 - exemption) * 0.05) + \
          (500000 * 0.20) + \
          ((income - 1000000) * 0.30)

# Displaying total tax
print("Total Tax to be paid:", tax)