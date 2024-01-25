numero1=float(input("Introduzca el primer número: "))
numero2=float(input("Introduzca el segundo número: "))

print("\nMenú:")
print("1. Mostrar suma")
print("2. Mostrar resta (primer número menos segundo número)")
print("3. Mostrar multiplicación")

opcion=input("Selecciona una opción (1-3): ")

while opcion not in ["1","2","3"]:
    print("La opción elegida no es válida.")
    opcion = input("Selecciona una opción válida (1-3): ")

opcion=int(opcion)

if opcion == 1:
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == 2:
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
elif opcion == 3:
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
