income = float(input("Enter your monthly income:"))
expense = float(input("Enter your total monthly expenses:"))
monthly_saving = income - expense
total_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print("Your monthly savings are $",monthly_saving)
print("Projected savings after one year, with interest, is: $",total_savings)