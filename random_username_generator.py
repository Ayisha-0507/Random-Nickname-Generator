
import random

# Lists of adjectives and nouns for username generation
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

    return username[:length]  # Truncate to required length

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for name in usernames:
            file.write(name + "\n")
    print(f"Usernames saved to {filename}")

# Generate a list of usernames automatically
num_usernames = 10  # Number of usernames to generate
usernames_list = [generate_username() for _ in range(num_usernames)]

# Save usernames to a file
save_usernames(usernames_list)
