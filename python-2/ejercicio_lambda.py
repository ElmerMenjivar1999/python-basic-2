PI = 3.14159265359

radio_input = int(input("Digite el radio del circulo: "))

calcular_area = lambda radio: PI * radio * radio
#redondeando el resultado
area = round(calcular_area(radio_input),2)

print(f"El area del circulo es: {area} cm")
