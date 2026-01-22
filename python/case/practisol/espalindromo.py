#determinar si es palindromo una letra

leter = input("ingrese letra")

leter_inverso = ""
for i in reversed(leter):

    leter_inverso += i



if leter_inverso == leter:

    print("palindrom")
else:

    print("no es palindromo")
    

