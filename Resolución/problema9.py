num_elementos = int(input("Ingrese el número de elementos en la lista: "))

mi_lista = []
for i in range(num_elementos):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    mi_lista.append(elemento)
print("\nLista original:", mi_lista)
lista_invertida = mi_lista[::-1]
print("Lista invertida:", lista_invertida)
