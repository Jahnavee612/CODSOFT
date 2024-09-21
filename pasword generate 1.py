import secrets
import string

def generate_password(length=12):
    """Generate a secure random password."""
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    
    # Define the character sets
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits          # 0-9
    punctuation = string.punctuation  # special characters

    # Combine all the character sets
    all_characters = letters + digits + punctuation
    
    # Generate a secure password
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    if password:
        print(f"Generated password: {password}")
