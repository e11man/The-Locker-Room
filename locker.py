import requests
import string
import argparse

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols):
    """Generates a password with customizable character sets."""
    if length <= 0:
        raise ValueError("Password length must be positive.")

    characters = []
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Make a single, larger request to RANDOM.ORG 
    response = requests.get(f"https://www.random.org/integers/?num={length}&min=0&max={len(characters)-1}&col=1&base=10&format=plain")

    try:
        indices = map(int, response.text.strip().split("\n"))
        password = ''.join(characters[i] for i in indices)
        return password 
    except requests.exceptions.RequestException:
        print("Error: Could not fetch random data from RANDOM.ORG.")
        return None  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random password using RANDOM.ORG.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols")
    args = parser.parse_args()

    password = generate_password(args.length, args.lowercase, args.uppercase, args.digits, args.symbols)
    if password:
        print("Your new password is:", password)
