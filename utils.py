def getFloatInput(inputStatment):
    """ helper method to get float value from user 
    
        Args:
            inputStatement str: input string to be print for user
        
        Return:
            float: returns the float value of user input
        
        Raises:
            Errors: if user enters chars error will be displayed and ask user
                to re-enter the value
    """
    while True:
        f_str_value = input(inputStatment)
        if f_str_value.replace(',','').replace('.','').isdigit():
            return float(f_str_value.replace(',',''))
        else:
            print("\n Invalid input. Valid format : \n" +
                  " 1234.56, 12345, 1,234, 1,234.33 \n")

def getIntInput(inputStatment):
    """ helper method to get integer value from user
    
        Args:
            inputStatement str: input string to be print for user
        
        Return:
            int: returns the integer value of user input
        
        Raises:
            Errors: if user enters any value other digit error will be 
                displayed and ask user to re-enter the value
    """
    while True:
        m_str_value = input(inputStatment)
        if m_str_value.replace(',','').isdigit():
            return int(m_str_value)
        else:
            print("\n Invalid input. Valid formats: 123, 1,234 \n")

def getDays(months):
    month_days = {
        1: 31,
        2: 59,
        3: 90,
        4: 120,
        5: 151,
        6: 181,
        7: 212,
        8: 243,
        9: 273,
        10: 304,
        11: 334,
        12: 365
    }

    if months > 12:
        return ((months//12) * month_days[12]) + (month_days[(months % 12)]) 
    else:
        return (month_days[months]) 

