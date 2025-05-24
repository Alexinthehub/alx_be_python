def main():
    # Get user inputs
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Annual savings without interest
    annual_savings = monthly_savings * 12

    # Calculate projected savings after 1 year with 5% interest
    interest_rate = 0.05
    projected_savings = annual_savings + (annual_savings * interest_rate)

     # Output results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

if __name__ == "__main__":
    main()
