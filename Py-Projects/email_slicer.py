email=input("Enter your email :")
index= email.index("@")
username= email[:index]
domain=email[index+1:]
print(f"yor user name is {username} and domian is {domain}")