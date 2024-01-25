mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Lista original:", mi_lista)

posiciones_a_eliminar = [0, 4, 5]

for i in sorted(posiciones_a_eliminar, reverse=True):
    if 0 <= i < len(mi_lista):
        mi_lista.pop(i)
print("Lista después de eliminar elementos en las posiciones 0, 4 y 5:", mi_lista)
