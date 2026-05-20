def multiplicar(num):

    with open("multiplicar.txt" , "w" , encoding="utf-8") as f :

        for i in range(1,11):
            
            f.write(f"{num} x {i} = {num * i}\n")



multiplicar(2)