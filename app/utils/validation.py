import re

class Validation:
    @staticmethod
    def is_valid_email(email):
        # Using regular expression to check email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, email)

    @staticmethod
    def is_valid_password(password):
        # Password length should be at least 8 characters
        return len(password) >= 8   

    @staticmethod
    def validate_user_input(name, email, password):
        if not name or not email or not password:
            return "Name, email, and password are required fields"

        if not Validation.is_valid_email(email):
            return "Invalid email format"

        if not Validation.is_valid_password(password):
            return "Password should be at least 8 characters long"

        return None  # Input is valid
