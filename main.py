import string
import random

# Getting all the alphabets
characters = list(string.ascii_letters)

# Adding numbers from 0 to 9 to the list
characters.extend(list(x for x in range(0, 10)))

# Adding all the Special Characters
characters.extend(list(string.punctuation))

# Main program to generate password
if __name__ == "__main__":
    size = int(input("Enter the Size of the Password: "))
    password = ''
    for i in range(size):
        password += str(random.choice(characters))
    print(password)