import time
my_time=int(input("enter time in second"))
for i in range(my_time,0,-1):
 second=i%60
 minutes=int(i/60)%60
 hour=int(i/3600)%24
 print(f"{hour:02}:{minutes:02}:{second:02}")

 time.sleep(1)
print("times up")