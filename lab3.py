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


# You are tasked with developing a Python program for a bank to help determine whether a customer is eligible for a loan based on their salary and loan amount requested.
# The customer is eligible for a loan if:

# Their monthly salary is greater than or equal to 30,000.00.
# The loan amount they request is less than or equal to 10 times their monthly salary.
# If customer is eligible, ask how many months to pay and add a 10% interest increase

# If the customer is not eligible, display a message explaining why they are not approved (either low salary or too high loan request)














