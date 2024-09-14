import random 
import string


text=string.digits+string.ascii_letters+string.punctuation
text=list(text)
key=text.copy()
random.shuffle(key)
user=input("enter a text :")
cyiper=""
for letter in user:
    index=text.index(letter)
    cyiper+=key[index]
    
print(f"the orginal text is {user}")
print(f"the encrypeted text is {cyiper}")