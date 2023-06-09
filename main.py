import pywhatkit

numTel=str(input("Ingrese el #:"))
mensaje=str(input("Ingrese el mensaje: "))
horas=int(input("Ingrese la hora: "))
minutos=int(input("Ingrese los minutos: "))

pywhatkit.sendwhatmsg("+51"+numTel, mensaje, horas, minutos, 4, True, 4)