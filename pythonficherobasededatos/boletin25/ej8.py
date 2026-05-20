origen="origen.txt"
destino="destino.txt"

try:
    with open(origen , "r" , encoding="utf-8") as f:
        entrada =f.readlines()
        error = True
        

        if ";" not in entrada: 
            error = False
        
        print(error)

except Exception :
    print("error ")