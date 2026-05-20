def login(usuario ,contraseña ):
    usuario_registrados = {}
    fichero = "/home/michael/pythonficherobasededatos/boletin23/login.txt"
    try:
        with open(fichero , "r" , encoding="utf-8") as f :
              

              if not f :
                 print("fichero vacio ")  
              
              for i in f :
                  a = i.strip().split()
                  
                  for p in a :
                       k , c  = p.split(":")
                       usuario_registrados[k] = c
        
        if usuario_registrados.get(usuario) is not None :
             if usuario_registrados.get(usuario) == contraseña:
                  print("valido")
             else:
                  print("contraseña incorrecta")
        else:
             print("usuario no encontrado  ")
             
    except FileNotFoundError:
         print("fichero inexistente o imposible acceder a el  ")
    

login("josemaria","abc")