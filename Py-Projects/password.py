import string
import secrets

print("WELCOME TO PASSWORD GENERATOR :")
print("1) STRING \n2) NUMBER \n3) ASCII")

ascii_letters = string.ascii_letters
digits = string.digits
ascii_digits = ascii_letters + digits

choice = int(input("What type of password do you need (1, 2, or 3): "))
length = int(input("Length of the password: "))

password_chars = ""
password = ""

while True:
    if choice == 1:
        password_chars = ascii_letters
        break
    elif choice == 2:
        password_chars = digits
        break
    elif choice == 3:
        password_chars = ascii_digits
        break
    else:
        print("Wrong choice. Please select 1, 2, or 3.")
        choice = int(input("What type of password do you need (1, 2, or 3): "))

for i in range(length):
    password += secrets.choice(password_chars)

print(f"Your generated password is: {password}")
