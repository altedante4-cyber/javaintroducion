
try:

    with open("texto4.txt","r")as f :

        entrada = f.readlines()

    palabras = [x[::-1] for x in entrada[::-1]]

    with open("nuevo.txt","w",encoding="utf-8") as f :

        f.write("".join(palabras))
    
except:
    print("Error")