foods=[]
price=[]
total=0
while True:
    ans=input("enter the foos that you want or press Q to quit :")
    if ans.lower()=="q":
        break
    else:
        prices=int(input("enter the price of the food :"))
        foods.append(ans)
        price.append(prices)
        
      
print("##########cart###############") 
for food in foods:
    print(food,end="")
for p in price :
    total+=prices
    
    
print(f"your total bill is : ${total}")
    