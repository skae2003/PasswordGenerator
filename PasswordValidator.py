import string

class PasswordValidator:
    def __init__(self):
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    def is_valid_password(self, password):
        # Check length
        if len(password) < 8:
            return False

        # Check for at least one uppercase letter
        if not any(char in self.uppercase_letters for char in password):
            return False

        # Check for at least one digit
        if not any(char in self.digits for char in password):
            return False

        # Check for at least one special character
        if not any(char in self.special_characters for char in password):
            return False

        return True

def main():
    password_validator = PasswordValidator()

    while True:
      user_input = input("Enter a password to check (or 'q' to quit): ")

      if user_input.lower() == 'q':
          print("Goodbye")
          break

      if password_validator.is_valid_password(user_input):
          print("Valid password!")
      else:
          print("Invalid password. Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")

if __name__ == "__main__":
  main()