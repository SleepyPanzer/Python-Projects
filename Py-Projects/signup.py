username=input("Enter User name :")
password=input("Enter password :")
print(f"username and password saved ")
print("login :")
username2=input("enter username :")
password2=input("Enter password :")

if username2==username and password==password2:
    print("logged in sucessfully")
elif username2==username and password!=password2:
    print("password is not right ")
elif username2!=username and password==password2:
    print("username worong ")
else:
    print("both wrong")