password = "ALaGrandeLePuseCuca"
passInput = ""

while(passInput != password):
    
    passInput = input("Ingrese la contraseña: ")
    if passInput == password :
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")