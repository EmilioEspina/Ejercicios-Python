print("Bienvenido a MI calculadora ")
print("1) Suma")
print("2) Resta")
print("3) Multiplicacion")
print("4) Division")

opc = int(input("Selecciona la operacíon: "))

if opc > 4 or opc < 0:
    print("QUE TE PASA")
else:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))


if opc == 1:
    num1 += num2
    print(f"El total es: {num1}")
elif opc ==2:
    num1 -= num2
    print(f"El total es: {num1}")
elif opc == 3:
    num1 *= num2
    print(f"El total es: {num1}")
elif opc == 4:
    if num1 == 0 or num2 == 0:
        print ("No se puede dividir por 0")
    else:
        num1 /= num2
        print(f"El total es: {num1}")

# num1 = random.randint(1, 100) / ejemplo de numero random