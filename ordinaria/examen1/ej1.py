import random
cont = 0 
for _ in range(5):

    for i in range(4):
             
        for j in range(5):
              print(random.randint(1,9) , end="")
              cont += 1
        if  i == 3:
            print("" ,end="")
        else:
             print("-",end="")
             cont = 0

    print()

