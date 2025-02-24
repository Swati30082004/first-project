import random
import string

# List of adjectives and nouns
adjectives = ['Cool', 'Happy', 'Mighty', 'Brave', 'Wild', 'Silent', 'Clever', 'Fierce', 'Swift', 'Lazy']
nouns = ['Tiger', 'Dragon', 'Lion', 'Eagle', 'Shark', 'Phoenix', 'Wolf', 'Panda', 'Bear', 'Whale']

def generate_username(include_numbers=False, include_special_chars=False, length=None):
    """Generate a random username based on user preferences."""
    
    # Combine random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    # Optional addition of numbers
    if include_numbers:
        number = random.randint(1, 999)
        username = f"{adjective}{noun}{number}"
    else:
        username = f"{adjective}{noun}"

    # Optional addition of special characters
    if include_special_chars:
        special_char = random.choice(string.punctuation)
        username += special_char

    # Optional length adjustment
    if length and len(username) > length:
        username = username[:length]

    return username

def save_usernames(usernames, filename="usernames.txt"):
    """Save the generated usernames to a file."""
    with open(filename, 'w') as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

def get_user_input():
    """Get preferences from the user."""
    print("Welcome to the Random Username Generator!")
    include_numbers = input("Include numbers in the usernames? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters in the usernames? (yes/no): ").strip().lower() == 'yes'
    length = input("Set a maximum length for the username (or press Enter to skip): ").strip()
    
    if length:
        length = int(length)
    else:
        length = None

    num_usernames = int(input("How many usernames would you like to generate? "))
    return include_numbers, include_special_chars, length, num_usernames

def main():
    include_numbers, include_special_chars, length, num_usernames = get_user_input()
    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]
    
    # Show generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    # Ask if user wants to save usernames to a file
    save_option = input("\nWould you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        save_usernames(usernames)

if __name__ == "__main__":
    main()
