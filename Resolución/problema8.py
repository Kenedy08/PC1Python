hora_ingresada = input("Ingrese la hora en formato de 24 horas (por ejemplo, 14:30): ")

try:
    horas, minutos = map(int, hora_ingresada.split(':'))
except ValueError:
    print("Formato de hora incorrecto. Por favor, ingrese la hora en formato HH:MM.")
    exit()

if 7 <= horas < 8:
    print("Es hora de desayunar.")
elif 12 <= horas < 13:
    print("Es hora de almorzar.")
elif 18 <= horas < 19:
    print("Es hora de cenar.")


