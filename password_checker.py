"""Password_checker.py
A simple password checker that verifies if a password meets certain criteria."""

import re
import sys

"""Check if the password meets the criteria"""

def check_password(pwd):
    # Check if the password is at least 8 characters long
    if len(pwd) < 8:
        return "Password must be at least 8 characters long."   
    else:
        # Check if the password contains at least one uppercase letter
        if not re.search(r'[A-Z]', pwd):
            return "Password must contain at least one uppercase letter."
        # Check if the password contains at least one lowercase letter
        elif not re.search(r'[a-z]', pwd):
            return "Password must contain at least one lowercase letter."
        # Check if the password contains at least one digit
        elif not re.search(r'\d', pwd):
            return "Password must contain at least one digit."
        # Check if the password contains at least one special character
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
            return "Password must contain at least one special character."
        else:
            return "Password is valid."
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python password_checker.py <password>")
        sys.exit(1)
    
    password = sys.argv[1]
    result = check_password(password)
    print(result)