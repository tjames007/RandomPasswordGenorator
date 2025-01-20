import random
import string

def get_user_input():
  """
  Gets user input for password generation parameters.

  Returns:
    A tuple containing:
      - password_length (int)
      - use_uppercase (bool)
      - use_lowercase (bool)
      - use_digits (bool)
      - use_symbols (bool)
  """
  while True:
    try:
      password_length = int(input("Enter desired password length: "))
      if password_length <= 0:
        print("Password length must be greater than 0.")
        continue

      use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
      use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
      use_digits = input("Include digits? (y/n): ").lower() == 'y'
      use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

      if not (use_uppercase or use_lowercase or use_digits or use_symbols):
        print("Error: At least one character type must be selected.")
        continue

      return password_length, use_uppercase, use_lowercase, use_digits, use_symbols

    except ValueError:
      print("Invalid input. Please enter a valid integer for password length.")

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
  """
  Generates a random password with customizable characteristics.

  Args:
    length: The desired length of the password.
    use_uppercase: True if uppercase letters should be included.
    use_lowercase: True if lowercase letters should be included.
    use_digits: True if digits (0-9) should be included.
    use_symbols: True if symbols should be included.

  Returns:
    The generated password as a string.
  """

  characters = ''
  if use_uppercase:
    characters += string.ascii_uppercase
  if use_lowercase:
    characters += string.ascii_lowercase
  if use_digits:
    characters += string.digits
  if use_symbols:
    characters += string.punctuation

  if not characters:
    return "Error: At least one character type must be selected."

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

if __name__ == "__main__":
  password_length, use_uppercase, use_lowercase, use_digits, use_symbols = get_user_input()
  generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_symbols)
  print("Generated Password:", generated_password)