# Import the create_cd_account and create_savings_account functions
import utils
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    line_len = 70
    print("-" * line_len)
    print(f"{'***** Welcome to AK Bank *****':^70}")
    print("-" * line_len)
   
    while True:
        print(f"\n Select an account to check balance and interest earned.\n")
        print(f" 1. Savings Account")
        print(f" 2. Certificate of Deposit")
        acnt_type = input('\n Enter your selection: ')
        match acnt_type:
            case '1': 
                print(f"\nEnter your Savings Account Details.\n")
                s_balance = utils.getFloatInput("Balance: ")
                s_int = utils.getFloatInput("Interest Rate: ")
                s_months = utils.getIntInput("Months: ")
                print("-" * line_len)

                # Call the create_savings_account function and pass the variables from the user.
                updated_savings_balance, s_interest_earned = create_savings_account(s_balance, s_int, s_months)

                # Print out the interest earned and updated savings account balance with interest earned for the given months.
                print(f"Current balance is {updated_savings_balance:,.2f}. \n"+
                    f"Interest Earned for {s_months} months is {s_interest_earned:,.2f} at the rate of {s_int}%.\n")
            case '2':
                # Prompt the user to set the CD balance, interest rate, and months for the CD account.
                print("-" * line_len)
                print(f"\nEnter your Certificate of Deposit Details.\n")
                cd_balance = utils.getFloatInput("Balance: ")
                cd_int = utils.getFloatInput("Interest Rate: ")
                cd_maturity = utils.getIntInput("Months: ")
                print("-" * line_len)

                # Call the create_cd_account function and pass the variables from the user.
                updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_int, cd_maturity)

                # Print out the interest earned and updated CD account balance with interest earned for the given months.
                print(f"Current balance is {updated_cd_balance:,.2f}. \n"+
                    f"Interest Earned for {cd_maturity} months is {cd_interest_earned:,.2f} at the rate of {cd_int}%.\n")
            case _:
                print(f"\nInvalid Selection.")
        
        if (input("\nEnter Y to check another account: ")).lower() == 'y':
            continue
        else:
            break

if __name__ == "__main__":
    # Call the main function.
    main()