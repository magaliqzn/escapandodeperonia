print ("""    ESCAPANDO DE PERONIA
1- NIVEL FACIL: Tincho con ciudadania europea
2- NIVEL MEDIO: Otaku en escuela pública
3- Nivel Dios: Nacido en Formosa""")
       
answer = input (" ELIGE EL NIVEL [1//2/3]")

#nivel facil

if answer.lower().strip()== "1":
    
    answer = input (" ¿Elegiste nivel facil?   Eso es aburrido, estas aburriendo a todos, deja de aburrinos, seguro que quieres hacer nivel facil [si/no]").lower().strip()
    if answer == "si":
        answer = input (""" Tenes 18 años y vives comodamente en un country con tus padres, tu hermana pilar y dos perros cuyas razas fueron modificadas geneticamente para llevarlos en un bolso


                Un dia tus padres te regalan un viaje ¿donde eliges ir?
                1-viaje a miami
                2-cualquier otro lugar
                3-no me gusta viajar
                    elige 1/2/3""")
        if answer == "1":
            answer = input (" sos Ricardo FORT ? s/n")
            if answer == "s":
                answer = input (" GANASTE EL JUEGO, FELICIDADES COMANDANTE, LO EXTRAÑAMOS ")
            elif answer == ("n") :
                answer = input ("""GAME OVER
                Te quedas en la empresa de tu padre, ultrajas una empleada y mueres quemado en la plaza de tu ciudad en manos de feministas""")
            else:
            print ("no se qué apretaste pero seguro perdiste")
        elif answer == ("2"):
            answer = input (""" Luego de tu viaje a ;cualquier lado menos MIAMEEEEEEE; te das cuenta que tus país es muy decadente, pero un dia en una juntada de amigos/as
                              llega un inglés y dice *En Aryentina hay mushios pobres*, tu respondes
                              1- Si ojala fuera como la buena Gran Bretaña, allà seguro se vive bien
                              2- Callate modelo del gran libro de las sonrisas británicas, pobre tu vieja que te tiene que aguantar
                              3- *Te quedas callado, pues INTROVERTIDO*
                                      ELIGE 1/2/3""")
              if answer == "1":
                 answer = input ("""ese verano te vas a Inglaterra de viaje con tu novix, al llegar el/ella te abandona por un rubio ojos azules
                                    vuelves a tu casa triste feo/a y muerto/a por vendepatria - GAME OVER""")                               

              elif answer == "2":
                 
                 answer = input (""" el ingles se rie y te invita a su casa en Londres, en el verano vas te enamoras de él y te casas
                                      FELICIDADES LOGRASTE SALIR DE PERONIA """)
              elif answer == "3":
                 answer = input (""" la noche termina y te vas caminando, cuando de repente un linyera se acerca y te pide plata
                                    1- Lo cagas a piña con tus amigos rugbier
                                    2- Le das 1000 pesos argentino [10.8 dolares - año 2021] """)
                 if answer == "1":
                     answer = input ("""sos escrachado públicamente por una cuenta de troll de twitter llega a las 2 millones de visualizaciones y vos decidis
                                     1- Afrontar las consecuencias e ir preso
                                     2- Escapar en tu avion privado hacia una isla de Asia""")
                     if answer == "1":
                        answer = input ("Te meten a la carcel de Devoto, una noche tu compañero de celda te hace señorita, te contagias de SIDA y mueres 2 años después")
                     elif answer == "2":
                          answer = input ("Tú avion explota antes de despegar, mueres en Peronia, GAME OVER")
                     else:
                        print ("uno, dos, uno, dos, uno, dos.... OPCIÓN NO VALIDA")

                 elif answer == "2":   
                     answer = input ("""Resulta que el linyera era Jeff Bezos, que se emociona por tu acto de bondad y te ofrece trabajar en su empresa, tú:
                                    1- ACEPTAS    2- RECHAZAS """)
                     
    

                
        
    else:
        print ("ea... y bueno, chau entonces")
#nivel medio
elif answer == ("2"):
     answer = input (""" ¡ARIGATO GOZAIMASU SEMPAI¡ (suena un hentai en tu samsung j7 mientras tu madre entra abruptamente a tu sucia habitación
                        1- escondes el telefono pero el sonido sigue saliendo
                        2- tiras el telefono por la ventana
                        3- le mostras lo que estas viendo a tu madre
                                  elige 1/2/3""")

#nivel dios
elif answer == ("3"):
     answer = input ("""tsitsitsitsitsi.... se escucha la chicharra, te levanta de tu insufrible siesta abajo de un árbol de mango, hacen 40 grados y decides
                    1- preparar un tereré
                    2- ponerte repelente de mosquitos
                    3- ir a pasear a la costanera""")
else:
    print (" 1 2 o 3 dije, no es muy dificil")

                     
