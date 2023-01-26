#IMPORTACION DE LIBRERIAS
import subprocess

#COMIENZO DEL JUEGO
print("\n                                         LAS CRONICAS DE GARGAROTH           ")
print("                                        ---------------------------          ")
print("\nNi sabes como, te encuentras en Gargaroth, el pais del crimen y los monstruos, te despertaste en un coche de caballos en Valcalona y asumiste que tenias algo que hacer alli, pero cuando te cuestionaste quien eras y que hacias alli, le preguntaste a el conductor por tu nombre.")
nombre = input("\nElige un nombre -> ")
print("\n-Caballero, quien soy?")
print("-Eres " + nombre + ", el legendario guerrero Hispano que ha vencido a 600 dragones en una sola batalla, los habitantes de Gargaroth te adoran y eres un semidios en estas tierras.")

#DEFINICION DE VIDA Y RESTA
vida = 100
resta = 10
#FINAL DE VIDA Y RESTA

#COMIENZO DEL NIVEL 1
print("\n\n\n\nPRIMERA AVENTURA \n\n\nTe encuentras en Gargaroth, en la ciudad de Valcalona, cuando un campesino te pide ayuda.")
print("-Ayuda, hay un dragon - dice desesperado")
print("-No te preocupes, ya pensare que hacer - le respondes")

seguir1 = input("Seguir (presiona Enter)->")

print("\n1-Huyes")
print("2-Luchas")
print("3-Pides ayuda")

print("\nVida =", vida)

jugador_nivel1 = input("\nQue haces? ")

vida_dragon_nivel1 = 150
respuesta1_nivel1 = "1"
respuesta2_nivel1 = "2"
respuesta3_nivel1 = "3"

if jugador_nivel1 == respuesta2_nivel1:
    print("\nLE HAS QUITADO 50 DE VIDA")

    vida_dragon_nivel1 = vida_dragon_nivel1 - 50

    print("\nVida del dragon :", + vida_dragon_nivel1)
    print("\nEl dragon ataca y te quita 20 de vida")

    vida = vida - resta - resta

    print("\n\nTu vida :", + vida)
    print("\n\n1-Rendirte")
    print("2-Seguir con la batalla")

    respuesta1_2_nivel1 = "1"
    respuesta2_2_nivel1 = "2"

    decision1_nivel1 = input("\nQuieres huir o seguir con la batalla? -> ")

    if decision1_nivel1 == respuesta1_2_nivel1:
        print("Has abandonado y el dragon ha muerto desangrado, has salvado a Valcalona")
    else: 
        print("El dragon a lanzado una bola de fuego y ha acabado contigo")

else:
    print("10 MENOS DE VIDA")
    vida = vida - resta
    print(vida)
    print("\n1-Rendirte")
    print("2-Seguir con la batalla")
    decision_else1_nivel1 = input("Que quieres hacer? -> ")
    respuesta_1_3_nivel1 = "1"
    respuesta_2_3_nivel1 = "2"
    if decision_else1_nivel1 == respuesta_1_3_nivel1:
        print("Has decidido seguir luchando y has vencido al dragon, has salvado a Valcalona")
#FINAL DEL NIVEL 1