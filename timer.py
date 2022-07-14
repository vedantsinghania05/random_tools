from time import time, sleep

def timer(amount):
  start = time()
  for i in range(0, amount): 
    print(i, end="\r")
    sleep(1)
  end = time()
  print(end - (start + 0.0015 * amount))

timer(int(input("How many seconds? ")))