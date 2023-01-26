#IMPORTACION DE LIBRERIAS
import subprocess

#COMIENZO DEL JUEGO
print("\n                                         THE GARGAROTH CHRONICLES           ")
print("                                        --------------------------          ")
print("\nYou don't know how you are in Gargaroth, the crime and monsters country, but you think that you have something to do in that country, 2 days later, you are in Valcalona, Gargaroth. You ask you ask the driver for your name.")
nombre = input("\nChoose a name -> ")
print("\n-Sir, what's my name?")
print("-You're " + nombre + ", a legendary warrior of Hispania, you are a semi-god in Gargaroth.")
seguir0 = input("\nPress enter to follow")

#DEFINICION DE VIDA Y RESTA
vida = 100
resta = 10
#FINAL DE VIDA Y RESTA

#COMIENZO DEL NIVEL 1
print("\n\n\n\nFIRST ADVENTURE \n\n\nYou're in Valcalona, Gargaroth, when a peasant asks you for help.")
print("-Help please, there is a dragon")
print("-Don't worry, I'll think what to do")

seguir1 = input("\nPress enter to follow")

print("\n1-Run away")
print("2-Fight with the dragon")
print("3-Ask for help")

print("\nHP =", vida)

jugador_nivel1 = input("\nWhat do you do? ")

vida_dragon_nivel1 = 150
respuesta1_nivel1 = "1"
respuesta2_nivel1 = "2"
respuesta3_nivel1 = "3"

if jugador_nivel1 == respuesta2_nivel1:
    print("\nTHE DRAGON LOSES 50 HEALTH POINTS")

    vida_dragon_nivel1 = vida_dragon_nivel1 - 50

    seguir2 = input("\nPress enter to continue")

    print("\nDRAGON HP :", + vida_dragon_nivel1)
    print("\nThe dragon attacks and you lose 20 HP")

    vida = vida - resta - resta

    print("\n\nHP :", + vida)
    print("\n\n1-Run away")
    print("2-Follow fighting")

    respuesta1_2_nivel1 = "1"
    respuesta2_2_nivel1 = "2"

    decision1_nivel1 = input("\nWhat do you want to do? -> ")

    if decision1_nivel1 == respuesta1_2_nivel1:
        print("You've runned away and the dragon has died by the wounds, you've saved Valcalona")    
    else: 
        print("The dragon kills you with a fireball")

else:
    print("The dragon cathes you and kick you")
    print("-10 HP")
    vida = vida - resta
    print(vida)
    print("\n1-Run away")
    print("2-Follow fighting")
    decision_else1_nivel1 = input("What do you want to do? -> ")
    respuesta_1_3_nivel1 = "1"
    respuesta_2_3_nivel1 = "2"
    if decision_else1_nivel1 == respuesta_2_3_nivel1:
        print("You've decided to follow fighting and you've saved Valcalona")
    else:
        print("You've decided to run away and the dragon destroys Valcalona")
#FINAL DEL NIVEL 1
