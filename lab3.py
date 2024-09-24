# input 
loan_amt = float(input("Enter Loan Amount: $"))
monthly_salary = float(input("Enter Monthly Salary:$"))

if monthly_salary >= 30000: 
    if loan_amt <= (monthly_salary * 10):
        months = int(input("How many months to pay: "))
        interest = loan_amt * 0.10
        new_loan_amt = loan_amt + interest
        payable = new_loan_amt / months
        
        print(f"to be paid monthly: ${payable:.2f}")
    else:
        print("Customer is not eligible due to too high loan request.")

else:
    print("Customer is not eligible due to low salary.")

