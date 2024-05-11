#Crear un programa de validación de usuario y contraseña (consultar usuario y
#contraseña), los únicos dos usuarios conectados son:
#User1: pedro Contraseña1: 1234
#User2: angel Contraseña2: a4s1
usuario= input("Ingresar usauario: ")
contraseña= input("Ingresar contraseña: ")
contraseña_1= "1234"
user_1= "pedro"
contraseña_2= "a4s1"
user_2= "angel"

if user_1 === usuario and contraseña == contraseña_1:
    print ("Es el usuario correcto")
if user_1 == usuario and contraseña != contraseña_1:
    print("El usuariio es correcto pero La contraseña no es correcta ")
if user_2 == usuario and contraseña == contraseña_2:
    print("Es el usuario es correcto")
if user_2 == usuario and contraseña != contraseña_2:
    print("El usuariio es correcto pero La contraseña no es correcta ")
else:
    print("El usuario y contraseña son incorrectos")