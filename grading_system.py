score = float(input("Enter your score: "))
total = float(input("Enter the total possible points: "))

if total <= 0:
    raise SystemExit("Total possible points must be greater than zero.")

percentage = (score / total) * 100
print(f"Your grade is {percentage:.2f}%")

weight = float(input("Enter the assignment weight (%): "))
contribution = (percentage / 100) * weight
print(f"This assignment adds {contribution:.2f} percentage points to your final grade.")