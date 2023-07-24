import re

def validation_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z-0-9-]+\.[a-zA-Z-0-9-.]+$"
    validation = re.findall(pattern,email)

    if validation:
        print(f"Su correo {email} es valido!. Bienvenido al sistema")
    else:
        print("Por favor digite un email valido")

user_email = input("Introduzca su email: ")
validation_email(user_email)

