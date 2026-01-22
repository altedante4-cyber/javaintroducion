num = input("numeros")

cont = {}


for c in num :
    if c not in cont:
        cont[c] = 1 
    for k , v in cont.items():
        
        if v == 1 :
            print(f"{v} numero{k}")
        else:

            print(f"{v} numero {k}")

    