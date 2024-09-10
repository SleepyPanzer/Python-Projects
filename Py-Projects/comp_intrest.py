import math
principle=0
rate=0
time=0
run=True

while  run:
    principle=float(input("Enter the principle :"))
    if principle<=0:
        print("invalid value ")
    else :
        break
        
        
while run :
     rate=float(input("Enter the rate :"))
     if rate<=0:
        print("invalid value ")
     else :
        break
    
    
while run :
     time=int(input("Enter the time :"))
     if time<=0:
        print("invalid value ")
     else :
        break
compound_intrest=pow((1+rate/100),time)*principle
print(f"the compound intrest is {compound_intrest:,} after time  {time}")
    
      