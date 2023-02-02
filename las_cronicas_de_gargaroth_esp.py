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

#COMIENZO DEL INTERMEDIO
print("-Bueno Jade, ya hemos terminado la batalla con el dragon, Valcalona ahora es libre, pero mi objetivo siempre sera ir contra Stalder. -Le dices a la tabernera")
print("-Sigo pensando que no es buena idea el luchar contra Stalder.") 
curarte1 = input("Quieres curarte? -Te dice -> ")

si = "si"
no = "no"
enter = ""

if curarte1 == si:
    vida = 100
    print("HP :", vida)
if curarte1 == no:
    print("-Bueno, la proxima batalla moriras.")
if curarte1 == enter:
    print("Por favor, escribe 1 o 2.")
#FIN DEL INTERMEDIO

#COMIENZO DEL NIVEL 2
print("\n\n\n\n\n\nTe encuentras en las afueras de Valcalona, preparado para cualquier cosa despues de derrotar a un dragon, cuando ves que un mago te llama.")
print("\n-" + nombre + ", Eres el legendario guerrero capaz de derrotar a cualquier monstruo?")
print("Sin querer decepcionarle pero sabiendo que no podias con todo, le respondes.")
print("-Emmm... si?")
print("-Genial porque ya necesitaba a alguien. En mi aldea, ha entrado el temible Volcrom, el ogro que ha asesinado a tantas personas en los territorios de Gargaroth.")
print("Con el corazon en la boca le respondes...")
print("-Y supongo que querras que acabe con el no?")
print("-Por favor acaba con el.")
print("Responde si o no")
pregunta_respuesta_1_nivel2 = input("Quieres salvar a su aldea? -> ")
if pregunta_respuesta_1_nivel2 == si:
    print("-Claro! Salvare a tu aldea encantado.")
    print("-Gracias a Dios, solo un guerrero como tu podria tener el valor de enfrentarse a Volcrom")
    seguir3 = input("Seguir (presiona Enter)")
    print("\nTe encuentras en la aldea del mago, y sin olvidar tu objetivo de asesinar a Stalder, te dirijes hacia el centro de la aldea donde ves a Volcrom arrasar con todo el poblado y piensas ''porque tuve que aceptar esta mision''.")
    print("\n\nVolcrom te ve y se dirije contra ti, tu, terriblemente asustado, decides sacar tu arma, cual quieres sacar?")
    print("1-Espada Valcaloniana")
    print("2-Hacha de los Bárbaros del norte")
    print("Responde con un numero")
    arma1_nivel2 = "1"
    arma2_nivel2 = "2"
    pregunta_respuesta2_nivel2 = input("\nElige una -> ")
    if pregunta_respuesta2_nivel2 == arma1_nivel2:
        print("Decides sacar la espada Valcaloniana obsequida por el alcalde de Valcalonia, pero mirando los detalles de la empuñadura, Volcrom te ataca y pierdes 50 HP")
        vida = vida - 50
        print("HP :", vida)
        print("Donde le atacas?")
        print("\n1-Cabeza")
        print("2-Rodillas")
        print("\nResponde con un numero")
        objetivo1_nivel2_Volcrom = "1"
        objetivo2_nivel2_Volcrom = "2"
        objetivo3_nivel2_Volcrom = "3"
        pregunta_respuesta3_nivel2 = input("A donde quieres atacar? -> ")
        if pregunta_respuesta3_nivel2 == objetivo1_nivel2_Volcrom:
            print("Le atacas en la cabeza y muere, has salvado a la aldea del mago.")
            print("-De verdad, muchas gracias por salvar por salvar a mi aldea.")
            print("El mago te obsequia con curacion al 100%")
            vida = 100
            print("HP :", vida)
            print("-Me unire a tu aventura. -Te dice")
        else:
            print("Le atacas en las rodillas y lo inmovilizas, pero te lanza la espada y te corta brutalmente la cabeza.")
            print("\n\n\n\n\n\n\n\nPresiona Ctrl+c para salir del juego.")
    else:
        print("Decides sacar el Hacha de los Bárbaros del norte, pero en un intento de levantarla Volcrom aprovecha y te asesina brutalmete cortandote la cabeza.")
        print("\n\n\n\n\n\n\n\nPresiona Ctrl+C para salir del juego.")
else:
    print("-Lo siento, he de reservar energias para la lucha contra Stalder.")
    print("-Tienes pensado luchar contra Stalder!!??")
    print("-Si, que pasa?")
    print("-Conoces la historia no?")
    respuesta1_1_2_nivel2 = "si"
    respuesta2_1_2_nivel2 = "no"
    pregunta_respuesta4_nivel2 = input("Quieres escucharla? -> ")
    if pregunta_respuesta4_nivel2 == respuesta1_1_2_nivel2: 
        print("\n\n-Hace mucho tiempo, en Gargaroth, mandaba un rey llamado Stalder. Ese rey tenía una hija muy bella llamada Helena. Helena enfermó, y el rey cayó en una gran depresion, pero la ocultaba porque sabia que no volveria a ver a su hija. Cuando la joven murio, aparecio con un puñal clavado, al principio, el rey sospechaba de su sirviente, asi que lo mato, hasta que empezo a sospechar de mas personas y ahora ya no confia en nadie.")
        print("Dicen que es el ser mas poderoso en el universo. -Te dice.")
        print("-Pero el en un intento de vengar a su hija me arrebato a mi familia.")
        print("-Bueno, al menos deja que te acompañe.")
        print("-Claro! Me serviras para acabar con Stalder.")
#FIN DEL NIVEL 2

