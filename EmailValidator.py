import re
def is_valid_email(email):
    """ Validates if the email address is in the format username@gmail.com """
    regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    if re.match(regex, email):
        return True
    else:
        return False
def is_valid_password(password):
    """ Validates if the password contains:- At least one uppercase letter- At least one lowercase letter- At least one digit- At least one special character (@, $, &, etc.)"""
    if (len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[@$&!#%^*]', password)):
        return True
    else:
        return False
def validate_credentials(email, password):
    """ Validates the email and password using the above functions and returns appropriate messages."""
    if is_valid_email(email):
        if is_valid_password(password):
             return "Valid email and password."
        else:
            return ("Invalid password. Make sure it contains at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.")
    else:
        return "Invalid email. Make sure it follows the format: username@gmail.com."
def submit(email, password):
    """ Function to simulate the submission process.It prints the result of the validation process. """ 
    validation_result =validate_credentials(email, password)
    print(validation_result)
email = input("Enter your email: ")
password = input("Enter your password: ")
submit(email, password)