consumo=float(input("¿Cuánto fue su consumo en soles en el restaurante?: "))
porcentaje=float(input("¿Qué porcentaje de propina desea dejar al mesero?: "))
propina=consumo*porcentaje/100
print(f'¡Perfecto!, la propina a dejar es de {propina} soles')
