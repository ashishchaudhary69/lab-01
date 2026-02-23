

# Taking cart value input
cart_value = float(input("Enter cart value: "))

# Taking membership type input
membership = input("Enter membership (Silver/Gold/Platinum): ").lower()

# Checking festival season
festival = input("Is it festival season? (yes/no): ").lower()

# List to store all possible discounts
discounts = []

# Cart value based discount
if cart_value > 10000:
    discounts.append(cart_value * 0.10)

# Membership based discount
if membership == "silver":
    discounts.append(cart_value * 0.05)
elif membership == "gold":
    discounts.append(cart_value * 0.10)
elif membership == "platinum":
    discounts.append(cart_value * 0.15)

# Festival season discount
if festival == "yes":
    discounts.append(cart_value * 0.20)

# Selecting highest discount
if discounts:
    max_discount = max(discounts)
else:
    max_discount = 0

# Calculating final amount
final_amount = cart_value - max_discount

# Display results
print("Highest Discount:", max_discount)
print("Final Payable Amount:", final_amount)