

# Taking percentage input
percentage = float(input("Enter 12th grade percentage: "))

# Checking if Mathematics was studied
maths = input("Did you study Mathematics? (yes/no): ").lower()

# Taking entrance exam score
entrance_score = int(input("Enter entrance exam score: "))

# Checking eligibility conditions one by one
if percentage < 75:
    print("Not eligible: Minimum 75% required.")

elif maths != "yes":
    print("Not eligible: Mathematics subject is required.")

elif entrance_score < 80:
    print("Not eligible: Entrance exam score must be at least 80.")

else:
    print("Congratulations! You are eligible for admission.")