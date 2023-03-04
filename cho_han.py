import random as rd
cartera=10
gana=0
continuar= "si"
print("***Bienvenido al juego de los daditos***")
print("*Usted tiene ${} en la cartera".format(cartera))
while cartera > 0 and continuar=="si":
    apuesta=int(input("Ingresa una apuesta: "))
    if apuesta <= cartera:
        dado1=rd.randint(1,6)
        dado2=rd.randint(1,6)
        total=dado1+dado2
        resto=total%2
        parimpar=input("Adivina ¿Par o impar? ")
        print("El resultado es: {} + {} = {}".format(dado1, dado2, total))
        if resto==0 and parimpar=="par":
            cartera+=apuesta
            gana+=1
        elif resto !=0 and parimpar=="impar":
            print("¡Ganaste!")
            cartera+=apuesta
            gana+=1
        else:
            print("¡Perdiste!")
            cartera-=apuesta
        print("Cartera: {}".format(cartera))
        if cartera!=0:
            continuar = input("¿Desea continuar jugando?")
            print("*************************")
    else:
        print("La apuesta excede su dinero en cartera")
print("Usted ganó {} partidas".format(gana))
print("***Muchas gracias por jugar***")