import random
adjectives = ["Cool", "Happy", "Brave", "Swift", "Mighty", "Clever", "Lucky", "Fierce"]
nouns = ["Tiger", "Dragon", "Phoenix", "Wolf", "Eagle", "Panther", "Shark", "Falcon"]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, length=10):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if include_numbers:
        username += str(random.randint(10, 99))  # Adding two-digit number

    if include_special_chars:
        special_chars = "!@#$%^&*"
        username += random.choice(special_chars)  # Adding a random special character

    return username[:length]  


usernames_list = []

# Get number of usernames to generate
num_usernames = int(input("Enter the number of usernames to generate: "))

for _ in range(num_usernames):
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    length_input = input("Enter username length (default 10): ").strip()
    length = int(length_input) if length_input.isdigit() else 10

    username = generate_username(include_numbers, include_special_chars, length)
    usernames_list.append(username)
    print(f"Generated Username: {username}")

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for name in usernames:
            file.write(name + "\n")
    print(f"Usernames saved to {filename}")

# Save the usernames
save_usernames(usernames_list)
