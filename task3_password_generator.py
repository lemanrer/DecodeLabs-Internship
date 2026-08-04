import secrets
import string

while True:
    try:
        length = int(input("Enter password length: "))
        if length<=0:
            print("Please enter a positive number.")
            continue
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(secrets.choice(characters) for i in range(length))
        break
    except ValueError:
        print("Invalid Data. Try again.")
        continue

print(f"Password: {password}")
