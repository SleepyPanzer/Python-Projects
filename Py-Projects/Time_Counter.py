import time

sec=int(input("Enter the time in second :"))
for i in range(sec,0,-1):
    seconds = i%60
    minute=int(i/60)%60
    hour=int(i/3600)
    print(f"{hour}:{minute}:{seconds}")
    time.sleep(1)
    
    