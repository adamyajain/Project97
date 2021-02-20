import random
num = random.randint(1,100)

turn = 0

while turn in  range(0,6):
  user = int(input("enter a number between 0-100: "))
  if user == 50:
    print("You Win")
  elif user > 50:
    print("this is greater than the desired number")
  else:
   print("this is less than the desired number")
  a+=1  
