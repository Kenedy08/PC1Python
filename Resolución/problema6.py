edad=int(input("¿Cuántos años tiene?: "))
if edad>0 and edad<4:
    input("Puede ingresar gratis a la sala de juegos")
elif edad >=4 and edad<=18:
    input("Para ingresar a la sala de juegos debes pagar $5")
else:
    input("Para ingresar a la sala de juegos debes pagar $10")
