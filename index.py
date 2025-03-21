# Este programa es acerca un prompt de inteligencia artificial

tiempo_soleado = bool(input("Escribe True o False segun sea el tiempo "))
temperatura = int(input("Escribe la temperatura "))
LLoviendo = input("Escribe si esta lloviendo ")

if tiempo_soleado == True and temperatura > 18:
    print("No va a llover")
    print("No tienes que llevar paragua ni abrigo")
elif tiempo_soleado == False and temperatura <18:
    print("Va a llover, tienes que llevar paraguas y tambien abrigo")
    print(LLoviendo)
else:
    print("Tranquila puedes ir a la playa")


