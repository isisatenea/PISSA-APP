from datetime import date
import random
from colorama import init, Fore, Back, Style
init()
#LECTURA
def lectora2(vidas):
    print("""GRIPE PROGRAMA DE ACOL PARA LA VACUNACIÓN VOLUNTARIA CONTRA LA GRIPE
Como usted probablemente ya sabe, la gripe se propaga rápida y extensamente durante el invierno. Los
que la sufren pueden estar enfermos durante semanas. La mejor manera de vencer a este virus es cuidar
lo más posible la salud de nuestro cuerpo. El ejercicio diario y una dieta rica en frutas y vegetales
es lo más recomendable para contribuir a que nuestro sistema inmunitario esté en buenas condiciones
para luchar contra el virus invasor. ACOL ha decidido ofrecer a su personal la oportunidad de
vacunarse contra la gripe, como recurso adicional para evitar que este insidioso virus se extienda
entre nosotros. 
ACOL ha previsto que una enfermera lleve a cabo el programa de vacunación dentro de la empresa en
horas de trabajo, durante la mitad de la jornada laboral de la semana del 17 de mayo. Este programa se
ofrece gratuitamente a todos los empleados de la empresa. 
La participación es voluntaria. Los empleados que decidan utilizar esta oportunidad deben firmar un
impreso manifestando su consentimiento e indicando que no padecen ningún tipo de alergia y que
comprenden que pueden experimentar algunos efectos secundarios sin importancia. 
El asesoramiento médico indica que la inmunización no produce la gripe. No obstante, puede originar
algunos efectos secundarios como cansancio, fiebre ligera y molestias en el brazo. 

¿Quién debe vacunarse? 
Cualquiera que esté interesado en protegerse del virus. Esta vacunación está especialmente
recomendada para las personas mayores de 65 años y, al margen de la edad, para CUALQUIERA que padezca
alguna enfermedad crónica, especialmente si es de tipo cardíaco, pulmonar, bronquial o diabético.
Más información: http://www.mecd.gob.es/inee 
En el entorno de una oficina, TODAS LAS PERSONAS corren el riesgo de contraer la enfermedad. 

¿Quién no debe vacunarse?
Las personas que sean hipersensibles a los huevos, las que padezcan alguna enfermedad que produzca
fiebres altas y las mujeres embarazadas. Consulte con su doctor si está tomando alguna medicación o si
anteriormente ha sufrido reacciones adversas a la vacuna contra la gripe. 
Si usted quiere vacunarse durante la semana del 17 de mayo, por favor, avise a la jefa de personal,
Raquel Escribano, antes del viernes 7 de mayo. La fecha y la hora se fijarán conforme a la
disponibilidad de la enfermera, el número de participantes en la campaña y el horario más conveniente
para la mayoría de los empleados. Si quiere vacunarse para este invierno pero no puede hacerlo en las
fechas establecidas, por favor, comuníqueselo a Raquel. Quizá pueda fijarse una sesión de vacunación
alternativa si el número de personas es suficiente.
Para más información, contacte con Raquel en la extensión 5577. 
Raquel Escribano, directora del departamento de recursos humanos de una empresa llamada ACOL, preparó
la información que se presenta en esta página y en la anterior para distribuirla entre el personal de
la empresa ACOL. Responde a las preguntas que se formulan a continuación, teniendo en cuenta la
información que aparece en las hojas de información.
 """)
    ask1="""¿Cuál de las siguientes afirmaciones describe una característica del programa de
inmunización de ACOL contra la gripe?
A) Se darán clases de ejercicio físico durante el invierno. 
B) La vacunación se llevará a cabo durante las horas de trabajo. 
C) Se ofrecerá un pequeño bono a los participantes. 
D) Un médico pondrá las inyecciones.
"""
    ask2="""Esta hoja informativa sugiere que si uno quiere protegerse del virus de la gripe, la
inyección de una vacuna de la gripe es…
A) Más eficaz que el ejercicio y una dieta saludable, pero más arriesgada. 
B) Una buena idea, pero no un sustituto del ejercicio y la dieta saludable. 
C) Tan eficaz como el ejercicio y una dieta saludable y menos problemática.
D) No es necesaria si se hace ejercicio y se sigue una dieta sana. 
"""
    ask3="""¿Cuál es el objetivo principal del autor?
A) Advertir.
B) Divertir.
C) Informar.
D) Convencer."""
    ask4="""Según la hoja informativa, ¿cuál de estos empleados de la empresa debería contactar con
Raquel? 
A) Ramón, del almacén, que no quiere vacunarse porque prefiere confiar en su sistema inmunológico
natural.
B) Julia, de ventas, que quiere saber si el programa de vacunación es obligatorio. C Alicia, de
recepción, que querría vacunarse este invierno pero dará a luz dentro de dos meses.
D) Miguel, de contabilidad, al que le gustaría vacunarse pero tiene que salir de viaje la semana del
17 de mayo.  
"""
    list_ask=[ask1,ask2,ask3,ask4]
    list_ans=["B","B","C","D"]
    for veces in range(4):
        pregunta=list_ask[veces]
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Lectura")
        lectura(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            lectura(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            lectura(vidas)
    return vidas 
def lectora1(vidas):
    print("""HERRAMIENTAS CIENTÍFICAS DE LA POLICÍA
Se ha cometido un asesinato, pero el sospechoso lo niega todo. Afirma no conocer a la víctima. Dice que nunca le había visto,
que nunca estuvo cerca de él, que nunca le tocó... La policía y el juez están convencidos de que no dice la verdad. Pero, ¿cómo
probarlo? En la escena del crimen, los investigadores han reunido hasta la más mínima evidencia: fibras de tela, cabellos,
huellas dactilares, colillas... Los pocos cabellos encontrados en la chaqueta de la víctima son pelirrojos. Y coinciden sospechosamente
con los del sospechoso. Si se pudiera probar que estos cabellos son realmente suyos, sería una prueba de que él conocía efectivamente a
la víctima. 
Cada persona es única Los especialistas se pusieron manos a la obra. Examinaron algunas células de la raíz de estos cabellos y algunas
células sanguíneas del sospechoso. En el núcleo de cada célula de nuestro cuerpo hay ADN. ¿Qué es eso? El ADN es como un collar hecho de
dos cadenas de perlas enroscadas. Imagine que estas perlas son de cuatro colores diferentes y que miles de estas perlas de colores (que
forman un gen) están dispuestas en un orden muy específico. En cada individuo este orden es exactamente el mismo en todas las células del
cuerpo: tanto en las de las raíces del cabello como en las del dedo gordo del pie, las del hígado y las del estómago o la sangre. 
Pero el orden de las perlas varía de una persona a otra. Dado el número de perlas dispuestas de este modo, hay muy pocas probabilidades de
que haya dos personas con el mismo ADN, salvo los gemelos idénticos. Como es único para cada individuo, el ADN es como un carnet de identidad
genético. Por lo tanto, los especialistas en genética son capaces de comparar el carnet de identidad genético del sospechoso (determinado
por su sangre) con el de la persona pelirroja. Si el carnet genético es el mismo, sabrán que el sospechoso estuvo en efecto cerca de la
víctima que según él nunca había visto. Sólo una prueba Cada vez con mayor frecuencia en casos de abusos sexuales, asesinato, robo o delitos,
la policía hace análisis genéticos. ¿Por qué? Para intentar encontrar evidencias de contacto entre dos personas, dos objetos o una persona y un
objeto. Probar dicho contacto suele ser muy útil para la investigación. Pero no proporciona necesariamente la prueba de un delito. Es sólouna prueba
entre muchas otras. Estamos formados por billones de células. Todo ser viviente está formado por muchísimas células. Una célula es realmente muy
pequeña. Incluso puede decirse que es microscópica porque sólo puede verse con la ayuda de un microscopio que la aumenta múltiples veces.
Cada célula tiene una membrana exterior y un núcleo en el que se encuentra el ADN. ¿Carnet de identidad genético? El ADN está formado por
un conjunto de genes, estando formado cada uno de ellos por miles de perlas. Todos estos genes juntos forman el carnet de identidad genético
de una persona. ¿Cómo se identifica el carnet de identidad genético? 
El especialista en genética coge unas pocas células de la base de los cabellos encontrados en la víctima, o de la saliva dejada en una colilla.
Las mete en un producto que elimina todo lo que hay alrededor del ADN de las células. Después, hace lo mismo con algunas células de la sangre
del sospechoso. Luego, el ADN se prepara especialmente para su análisis. Más tarde, se introduce en un gel especial y se hace pasar una corriente
eléctrica a través del gel. Al cabo de unas pocas horas, este procedimiento produce unas barras como si fueran un código de barras (similares a
las que se encuentran en los artículos que compramos) que son visibles bajo una lámpara especial. A continuación, el código de barras del ADN del
sospechoso se compara con el de los cabellos encontrados en la víctima.
 """)
    ask1="""Para explicar la estructura del ADN, el autor habla de un collar de perlas. ¿Cómo varía este collar de perlas de una persona a otra?
A) Varía en longitud. 
B) El orden de las perlas es diferente.
C) El número de collares es diferente.
D) El color de las perlas es diferente."""
    ask2="""¿Cuál es el propósito del recuadro titulado “¿Cómo se identifica el carnet de identidad genético?”
A) Lo que es el ADN.
B) Lo que es un código de barras.
C) Cómo se analizan las células para encontrar el patrón del ADN.
D) Cómo se puede probar que se ha cometido un crimen"""
    ask3="""¿Cuál es el objetivo principal del autor?
A) Advertir.
B) Divertir.
C) Informar.
D) Convencer."""
    ask4="""El final de la introducción (el primer recuadro sombreado) dice: “Pero ¿cómo probarlo?”. Según el texto, los investigadores intentan encontrar una respuesta a esta pregunta... 
A) Interrogando a los testigos. 
B) Realizando análisis genéticos.
C) Interrogando meticulosamente al sospechoso.
D) Volviendo sobre todos los hallazgos de la investigación de nuevo."""
    list_ask=[ask1,ask2,ask3,ask4]
    list_ans=["B","C","C","B"]
    for veces in range(4):
        pregunta=list_ask[veces]
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Lectura")
        lectura(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            lectura(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            lectura(vidas)
    return vidas
#MATEMATICAS [CRÉDITOS:JESUS CARLOS DUEÑAS ANDALON]
def estadistica(vidas):
    ask1="""Para descomponerse totalmente, a una piel de plátano le toman 1-3 años, a una piel de
naranja 1-3 años, a una cajas de cartón medio año, a un chicle 20-25 años, a un periódico unos pocos
días y a un vaso de plástico más de 100 años.
¿Por qué no sería buena idea representar esto en un diagrama de barras?
A) La diferencia de la longitud de barras sería muy grande.
B) Es mejor un pictograma.
C) El tiempo de descomposición de un vaso de plástico es indeterminado.
D) A y C
"""
    ask2="""Se mide la estatura de todos los alumnos en un salón. La estatura media de los hombres es
de 160 cm y la estatura media de las mujeres es de 150 cm. Elena ha sido la más alta (mide 180 cm).
Pedro ha sido el más bajo (mide 130 cm).
Dos estudiantes faltaron a clase ese día, pero fueron a clase al día siguiente. Se midieron sus
estaturas y se volvieron a calcular las medias. Sorprendentemente, la estatura media de las mujeres y
la estatura media de los hombres no cambió. Con esta información, podemos determinar:
A) Los dos estudiantes que faltaron eran mujeres.
B) Uno de los que faltó era hombre y el otro mujer.
C) Pedro sigue siendo el más bajo.
D) Ninguna de las anteriores.
"""
    ask3="""En el colegio de Irene, su profesora de ciencias les hace exámenes que se puntúan de 0 a
100. Irene tiene una media de 60 puntos en sus primeros cuatro exámenes de ciencias. En el quinto
examen sacó 80 puntos. ¿Cuál es su promedio?
A) 67 puntos  B) 61 puntos  C) 55 puntos  D) 64 puntos
"""
    ask4="""En una clase con 25 mujeres, la estatura promedio es de 1.30 metros. De las siguientes
afirmaciones, la única correcta es:
A) La estatura de la mayoría es de 130 cm.
B) Si se ordenan las chicas de la más baja a la más alta, entonces la estatura de la que ocupa la
posición central tiene que ser igual a 130 cm.
C) Si una de las mujeres de la clase mide 132 cm, tiene que haber otra de 128 cm de estatura.
D) Ninguna de las anteriores.
"""
    ask5="""Si en una clase de 25 mujeres hay una estatura promedio de 1.30 metros, pero luego se
descubre que una de las alumnas medía 1.20 metros en lugar de 1.54, ¿cuál es la altura promedio
correcta?
A) 1.26m  B) 1.27m  C) 1.28m  D) 1.29m
"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","C","A","B","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Matemáticas")
        mate(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    return vidas
#[CRÉDITOS:JESUS CARLOS DUEÑAS ANDALON]
def probabilidad(vidas):
    ask1="""La madre de Roberto le deja tomar un caramelo de una bolsa. Él no puede ver los caramelos. El número de caramelos de cada color que hay en la bolsa es el siguiente:
Rojos: 6
Anaranjados: 5
Amarillos: 3
Verdes: 3
Azules: 2
Rosas: 4
Morados: 2
Cafés: 5
¿Cuál es la probabilidad de que saque uno rojo?
A) 5%  B) 10)%  C) 20%  D) 30%
"""
    ask2="""Se realizaron varios sondeos de opinión para conocer el nivel de respaldo al Presidente
en las próximas elecciones. Cuatro periódicos hicieron sondeos por separado en toda la nación.
Los resultados de los sondeos de los cuatro periódicos se muestran a continuación:
Periódico 1: 36,5% (sondeo realizado el 6 de enero, con una muestra de 500
ciudadanos elegidos al azar y con derecho a voto).
Periódico 2: 41,0% (sondeo realizado el 20 de enero, con una muestra de 500
ciudadanos elegidos al azar y con derecho a voto).
Periódico 3: 39,0% (sondeo realizado el 20 de enero, con una muestra de 1.000
ciudadanos elegidos al azar y con derecho a voto).
Periódico 4: 44,5% (sondeo realizado el 20 de enero, con 1.000 lectores que llamaron
por teléfono para votar).
¿Cuál de los resultados de los periódicos sería la mejor predicción del nivel de apoyo al presidente?
A) El primero  B) El segundo  C) El tercero  D) El cuarto
"""
    ask3="""En una pizzería se puede elegir una pizza básica con dos ingredientes: queso y tomate.
También puedes diseñar tu propia pizza con ingredientes adicionales. Se pueden seleccionar entre
cuatro ingredientes adicionales diferentes: aceitunas, jamón, champiñones y salami. Jaime quiere
encargar una pizza con dos ingredientes adicionales diferentes. ¿Cuántas combinaciones diferentes
podría seleccionar?
A) 6  B) 8  C) 10  D) 12
"""
    ask4="""Un geólogo afirmó que en los próximos veinte años, hay dos posibilidades por cada 3 de
que ocurra un terremoto en la ciudad de Zed. 
¿Cuál de las siguientes opciones refleja mejor el significado de la afirmación del geólogo? 
A) ⅔ * 20 = 13.33 , así que entre 13 y 14 años a partir de ahora habrá un terremoto.
B) 3/2 es más que / 1 , por lo que se puede estar seguro de que habrá un terremoto en algún momento
en los próximos 20 años. 
C) La probabilidad de que haya un terremoto en algún momento en los próximos 20 años es mayor que
la probabilidad de que no haya ningún terremoto. 
D) No se puede decir lo que sucederá, porque nadie puede estar seguro de cuándo tendrá lugar un
terremoto. 
"""
    ask5="""¿Cuál es la probabilidad de obtener un cinco al lanzar un dado?
A) 40%  B) 17.5%  C) 23.34%  C) 16.67%
"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","C","A","B","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Matemáticas")
        mate(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    return vidas
#[CRÉDITOS:JESUS CARLOS DUEÑAS ANDALON]
def functions(vidas):
    ask1="""Una foca tiene que respirar incluso si está durmiendo dentro del agua. Martín observó una
foca durante una hora. Cuando empezó a observarla, la foca estaba en la superficie tomando aire.
Entonces se sumergió hasta el fondo del mar y comenzó a dormir. Desde el fondo invirtió 8 minutos en
subir lentamente a la superficie, donde tomó aire otra vez. Tres minutos después estaba de nuevo en el
fondo del mar. Martín se percató de que este proceso era muy regular. Al cabo de una hora, la foca
estaba:
A) En el fondo  B) Subiendo  C) Tomando aire  D) Bajando
"""
    ask2="""Por razones de salud la gente debería limitar sus esfuerzos, por ejemplo al hacer deporte,
para no superar una determinada frecuencia cardiaca. Durante años la relación entre la máxima
frecuencia cardiaca recomendada para una persona y su edad se describía mediante la fórmula siguiente:
Máxima frecuencia cardiaca recomendada = 220 – edad
Investigaciones recientes han demostrado que esta fórmula debería modificarse ligeramente. La nueva
fórmula es la siguiente: Máxima frecuencia cardiaca recomendada = 208 – (0,7 x edad).
¿A partir de qué edad aumenta la máxima frecuencia cardiaca recomendada como resultado de introducir
la nueva fórmula?
A) 40/41  B) 45/46  C) 53/54  D) 57/58
"""
    ask3="""La fórmula para la máxima frecuencia cardiaca recomendada = 208 – (0,7 x edad) se aplica
para determinar cuándo es más eficaz el ejercicio físico. Las investigaciones han demostrado que el
entrenamiento físico es más eficaz cuando la frecuencia cardiaca alcanza el 80% del valor máximo
recomendado.
Escribe una fórmula para hallar, en función de la edad, la frecuencia cardiaca recomendada para que el
ejercicio físico sea más efectivo.
A) 165 - 0.63 * edad
B) 170 - 0.65 * edad
C) 166 - 0.56 * edad
D) 164 - 0.54 * edad
"""
    ask4="""¿Cuáles son la pendiente y ordenada al origen de una función lineal que tiene las
coordenadas (4,2) y (0,-4)?
A) Pendiente de 5/4 y ordenada al origen de -4
B) Pendiente de 2/3 y ordenada al origen de -4
C) Pendiente de 3/2 y ordenada al origen de -3
D) Pendiente de 3/2 y ordenada al origen de -4
"""
    ask5="""¿Para dónde está la concavidad de la función y = (1-x)^2?
A) Hacia abajo  B) Hacia arriba  C) A y B  D) Ninguna de las anteriores
"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","C","A","B","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Matemáticas")
        mate(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    return vidas
#[CRÉDITOS:JESUS CARLOS DUEÑAS ANDALON]
def aritmetica(vidas):
    ask1="""Si un dólar vale 20.59 pesos mexicanos, y yo tengo 1500 dólares, ¿por cuántos pesos los
podría cambiar?
A) 30,886.80 pesos  B) 31,905.70 pesos  C) 27,654.40 pesos  D) 29,345.50 pesos
"""
    ask2="""Para construir una estantería un carpintero necesita lo siguiente:
4 tablas largas de madera
6 tablas cortas de madera
12 ganchos pequeños
2 ganchos grandes
14 tornillos
Si un carpintero tiene en el almacén 26 tablas largas de madera, 33 tablas cortas de madera, 200
ganchos pequeños, 20 ganchos grandes y 510 tornillos, ¿cuántas estanterías completas puede construir?
A) 3 estanterías  B) 7 estanterías  C) 5 estanterías  C) 6 estanterías
"""
    ask3="""Como consecuencia del calentamiento global del planeta, el hielo de algunos glaciares se
está derritiendo. Doce años después de que el hielo haya desaparecido, empiezan a crecer en las rocas
unas plantas diminutas, llamadas líquenes. Los líquenes crecen aproximadamente en forma de círculo.
La relación entre el diámetro de este círculo y la edad del liquen se puede expresar
aproximadamente mediante la fórmula:
d = 7 × (t −12)^(1/2) para t ≥12
siendo “d” el diámetro del liquen en milímetros, y “t” el número de años transcurridos
desde que el hielo ha desaparecido.
¿Cuál es el diámetro de un liquen 16 años después de que el hielo haya desaparecido?
A) 14mm  B) 20mm  C) 12mm  D) 9mm
"""
    ask4="""A una mujer ingresada en un hospital le ponen una inyección de penicilina. Su cuerpo va
descomponiendo gradualmente la penicilina de modo que, una hora después de la inyección, sólo el 60%
de la penicilina permanece activa. Esta pauta continúa: al final de cada hora solo permanece activo el
60% de la penicilina presente al final de la hora anterior. Supón que a la mujer se le ha administrado
una dosis de 300 miligramos de penicilina a las 8 de la mañana.
¿Cuántos miligramos tendrá activos en su sangre a las 11 de la mañana?
A) 108mg  B) 50mg  C) 70mg  D) 65mg
"""
    ask5="""Normalmente, una pareja de pingüinos pone dos huevos al año. Por lo general, el polluelo
del mayor de los dos huevos es el único que sobrevive. En el caso de los pingüinos de penacho
amarillo, el primer huevo pesa aproximadamente 78 g y el segundo huevo pesa aproximadamente 110 g.
Aproximadamente, ¿en qué porcentaje es más pesado el segundo huevo que el primer huevo?
A) 37%  B) 41%  C) 45% D) 53%
"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","C","A","B","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Matemáticas")
        mate(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    return vidas
#[CRÉDITOS:JESUS CARLOS DUEÑAS ANDALON]
def geometria(vidas):
    ask1="""Nicolás quiere pavimentar el patio rectangular de su nueva casa.
El patio mide 5,25 metros de largo y 3,00 metros de ancho. Nicolás necesita 81
ladrillos por metro cuadrado. ¿Cuántos ladrillos necesita para pavimentar todo el patio?
A) 1275/1276  B) 1867/1868  C)1115/1116  D)875/876
"""
    ask2="""Una pizzería sirve dos pizzas redondas del mismo grosor y de diferente tamaño.
La más pequeña tiene un diámetro de 30 cm y cuesta 30 euros.
La mayor tiene un diámetro de 40 cm y cuesta 40 euros. ¿Qué pizza tiene el mejor precio?
A) La mayor  B) La menor  C) Es lo mismo
"""
    ask3="""La estación espacial Mir permaneció en órbita 15 años y durante este tiempo dio
aproximadamente 86.500 vueltas alrededor de la Tierra. La permanencia más larga de un astronauta
en la Mir fue de 680 días. La Mir daba vueltas alrededor de la Tierra a una altura aproximada de
400 kilómetros. El diámetro de la Tierra mide aproximadamente 12.700 km y su circunferencia es de
alrededor de 40.000 km (π × 12.700). Calcula aproximadamente la distancia total recorrida por la Mir
durante sus 86.500 vueltas mientras estuvo en órbita. Da el resultado en millones de kilómetros.
A) 3200/3400 millones km  B) 3600/3800 millones km  B) 4000/4200 millones km  C) 4400/4600 millones km
"""
    ask4="""¿Cuántas veces más volumen tiene un cubo que una pirámide con su misma base y altura?
A) Dos veces  B) Tres veces C) 3.5 veces  D) La pirámide tiene más volumen
"""
    ask5="""¿Cuál es la suma de los ángulos internos de un triángulo?
A) 360°  B) 275°  C) 90°  D) 180°
"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","C","A","B","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de Matemáticas")
        mate(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            mate(vidas)
    return vidas
#PUNTOS EXTRAS [CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def extrasl(vidas):
    print("""La lectura trata sobre lo que acontece en una oficina médica. Fue ternura a primera vista. Llegó de la mano de su
padre, hurgó en el nuevo espacio intentando hacer un reconocimiento hasta que se dio cuenta de que era un espacio pequeño. Había
bebido de la mañana su mejor parte y se le escapaban rayitos de sol por los ojos. Parecía perderse entre las partículas de aire,
como hilvanando ficciones en un mundo alterno. —Iiiiiiii —era su única palabra, su única oración.
La repetía una y otra vez con distintos tonos, como si el cambio de tonos diera sentidos distintos a esa vocal.
Y Guillermo se convirtió en el explorador de aquella mañana de verano. Su mano, a veces, sin querer, tomaba la mía como buscando
afianzarse en un puente de amor inadvertido. Al mismo tiempo, alzaba un vuelo particular... escapando, lejos, muy lejos, de aquella
extraña y fría oficina. Su turno no llegaba y al parecer tardaría mucho más. Mientras el padre completaba unos formularios que
exigía el protocolo de la oficina, Guillermo caminaba; daba vueltas; se ponía en cuclillas; empezaba a contar los sueños que lleva
ba entre sus dedos, dedos que se transformaban en alas de duende; luego, daba con las manos tres golpes en el piso y seguía volando.
—Iiiiiiiiiiiiii —subía el tono de su melodía. Buscaba su “juguete” para decirle a su padre que se quería ir. “Caminar” —decía la
máquina, pero su padre no escuchaba, seguía llenando hojas y hojas detallando los pormenores de su historial. Creo que buscaba
aliento entre el papel y la tinta, antes de seguir imponiendo amor a su hijo nacido para despertar mariposas.
—Iiiiiiiiiiiii —argüía con carácter. Y cuando la puerta se abría, se escapaba para ir o para volver a cualquier parte, con su
mirada llena de luz. Yo estaba esperando también a que llamaran a mi hija. Habíamos ido allí buscándole solución a un problema raro.
Guillermo tropezaba una y otra vez con nuestras piernas y retomaba su vuelo, perdido en el tiempo y en el espacio. Al ritmo de
esta danza regresaba con sus alitas de duende a decirle a su padre iiiiiiiiiiiii. Era evidente que quería irse. Quise abrazarlo,
pero no me atreví. En un mundo en el que se intenta resguardar a los niños de la maldad cotidiana, no lo consideré apropiado.
Uuufff, hice un esfuerzo para contener las ganas, 
aunque lo abracé con el pensamiento, dirigida por su zigzagueante y profunda
mirada, buscando conectar con su frecuencia, con su hermosa vibración. Los niños que esperaban su turno miraban a Guillermo
asustados. Y sí, no había duda, Guillermo era especial. Por eso, quizá sin conocerlo me inspiró tanta ternura. La oficina fue
vaciándose. Mi hija ya estaba dentro con la doctora. Entonces el iiiiiii iiiii iiiii de Guillermo se intensificó, no quería
seguir esperando en ese lugar. Vi como sus manos se bamboleaban en el aire intentando capturar sus sueños. Guillermo escapaba
impetuosamente de la obligación de estar presente, daba tres golpes en el suelo, como agitando mariposas, le
nacían alas entre los dedos y transformaba aquella oficina en un solemne y misterioso mariposario.""")
    ask1="""¿Cuál de las siguientes opciones resume MEJOR la lectura?
A) El niño que cazaba mariposas
B) El comportamiento de un niño diferente
C) Las fantasías de Guillermo
D) La aburrida espera en una oficina médica"""
    ask2="""Según la lectura, se puede INFERIR que la máquina que usaba Guillermo era un....
A) juguete de la oficina con el que se entretenía
mientras esperaba.
B) instrumento electrónico que utilizaba el padre
para su trabajo.
C) procesador de palabras con el que jugaba todos
los días.
D) aparato que le permitía comunicarse porque no
podía hablar"""
    ask3="""De la lectura se puede INFERIR que Guillermo era un niño que...
A) se movía continuamente en su mundo
imaginario.
B) tenía dificultad para comunicarse con sus
hermanos.
C) todos los días jugaba con un amigo inventado.
D) sufría alucinaciones debido a los medicamentos."""
    ask4="""Según la lectura, Guillermo repite el sonido porque...
A) quiere marcharse de la oficina.
B) le teme a la mujer que lo observa.
C) está enojado con su padre.
D) pretende asustar a los otros niños."""
    ask5="""La mujer que observa al niño siente tanta ternura por él que quiere...
A) conocerlo.
B) abrazarlo.
C) besarlo.
D) protegerlo."""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["B","D","A","A","B"]
    list_user=[]
    cont=0
    while list_user!=list_ans or (list_user!=list_ans and list_ask!=[]):
        cont+=1
        pregunta=random.choice(list_ask)
        print()
        index_ask=list_ask.index(pregunta)
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {cont}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper()
        list_user.append(answer)
        while answer!=list_ans[index_ask]:
            pregunta=random.choice(list_ask)
            print()
            index_ask=list_ask.index(pregunta)
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {cont}. Lee con atención y contesta:                                          "+ Back.RESET)
            print(f"{pregunta}\n")
            answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper()
            list_user.append(answer)
    print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
    list_ans.remove(list_ans[index_ask])
    list_ask.remove(pregunta)
    list_user=[]
    vidas+=1
    print("Felicidades. Ganaste una vida extra")
    print(" ________________________________________________________________________")
    print("|Escoge entre estas 2 opciones:                                          |")
    print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
    print("|________________________________________________________________________|")
    print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
    opc=int(input(Fore.WHITE+"Opción seleccionada:"))
    if opc==1:
        menu(vidas)
    elif opc==2:
        lectura(vidas)
    return vidas
def extrasm(vidas):
    ask1="""La estación espacial Mir permaneció en órbita 15 años y durante este tiempo dio
aproximadamente 86.500 vueltas alrededor de la Tierra. La permanencia más larga de un astronauta
en la Mir fue de 680 días. La Mir daba vueltas alrededor de la Tierra a una altura aproximada de
400 kilómetros. El diámetro de la Tierra mide aproximadamente 12.700 km y su circunferencia es de
alrededor de 40.000 km (π × 12.700). Calcula aproximadamente la distancia total recorrida por la Mir
durante sus 86.500 vueltas mientras estuvo en órbita. Da el resultado en millones de kilómetros.
A) 3200/3400 millones km  B) 3600/3800 millones km  B) 4000/4200 millones km  C) 4400/4600 millones km."""
    ask2="""Normalmente, una pareja de pingüinos pone dos huevos al año. Por lo general, el polluelo
del mayor de los dos huevos es el único que sobrevive. En el caso de los pingüinos de penacho
amarillo, el primer huevo pesa aproximadamente 78 g y el segundo huevo pesa aproximadamente 110 g.
Aproximadamente, ¿en qué porcentaje es más pesado el segundo huevo que el primer huevo?
A) 37%  B) 41%  C) 45% D) 53%"""
    ask3="""Por razones de salud la gente debería limitar sus esfuerzos, por ejemplo al hacer deporte,
para no superar una determinada frecuencia cardiaca. Durante años la relación entre la máxima
frecuencia cardiaca recomendada para una persona y su edad se describía mediante la fórmula siguiente:
Máxima frecuencia cardiaca recomendada = 220 – edad
Investigaciones recientes han demostrado que esta fórmula debería modificarse ligeramente. La nueva
fórmula es la siguiente: Máxima frecuencia cardiaca recomendada = 208 – (0,7 x edad).
¿A partir de qué edad aumenta la máxima frecuencia cardiaca recomendada como resultado de introducir
la nueva fórmula?
A) 40/41  B) 45/46  C) 53/54  D) 57/58"""
    ask4="""En una pizzería se puede elegir una pizza básica con dos ingredientes: queso y tomate.
También puedes diseñar tu propia pizza con ingredientes adicionales. Se pueden seleccionar entre
cuatro ingredientes adicionales diferentes: aceitunas, jamón, champiñones y salami. Jaime quiere
encargar una pizza con dos ingredientes adicionales diferentes. ¿Cuántas combinaciones diferentes
podría seleccionar?
A) 6  B) 8  C) 10  D) 12"""
    ask5="""Un geólogo afirmó que en los próximos veinte años, hay dos posibilidades por cada 3 de
que ocurra un terremoto en la ciudad de Zed. 
¿Cuál de las siguientes opciones refleja mejor el significado de la afirmación del geólogo? 
A) ⅔ * 20 = 13.33 , así que entre 13 y 14 años a partir de ahora habrá un terremoto.
B) 3/2 es más que / 1 , por lo que se puede estar seguro de que habrá un terremoto en algún momento
en los próximos 20 años. 
C) La probabilidad de que haya un terremoto en algún momento en los próximos 20 años es mayor que
la probabilidad de que no haya ningún terremoto. 
D) No se puede decir lo que sucederá, porque nadie puede estar seguro de cuándo tendrá lugar un
terremoto."""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["B","A","C","A","B"]
    list_user=[]
    cont=0
    while list_user!=list_ans or (list_user!=list_ans and list_ask!=[]):
        cont+=1
        pregunta=random.choice(list_ask)
        print()
        index_ask=list_ask.index(pregunta)
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {cont}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper()
        list_user.append(answer)
        while answer!=list_ans[index_ask]:
            pregunta=random.choice(list_ask)
            print()
            index_ask=list_ask.index(pregunta)
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {cont}. Lee con atención y contesta:                                          "+ Back.RESET)
            print(f"{pregunta}\n")
            answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper()
            list_user.append(answer)
    print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
    list_ans.remove(list_ans[index_ask])
    list_ask.remove(pregunta)
    list_user=[]
    vidas+=1
    print("Felicidades. Ganaste una vida extra")
    print(" ________________________________________________________________________")
    print("|Escoge entre estas 2 opciones:                                          |")
    print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
    print("|________________________________________________________________________|")
    print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
    opc=int(input(Fore.WHITE+"Opción seleccionada:"))
    if opc==1:
        menu(vidas)
    elif opc==2:
        mate(vidas)
    return vidas
def extrasc(vidas):
    ask1="""El tabaco se fuma en forma de cigarrillos, puros o en pipa. Ciertas investigaciones
científicas han demostrado que las enfermedades relacionadas con el tabaco matan
cada día a unas 13.500 personas en el mundo. Se predice que, para 2020, las
enfermedades relacionadas con el tabaco originarán el 12 % del total de muertes.
El humo del tabaco contiene sustancias nocivas. Las sustancias más perjudiciales son
el alquitrán, la nicotina y el monóxido de carbono.
El humo del tabaco se inhala en los pulmones. El alquitrán del humo se deposita en
los pulmones y les impide funcionar de forma adecuada.

¿Cuál de las siguientes funciones es propia del pulmón?
A) Bombear sangre oxigenada a todas las partes del cuerpo.
B) Transferir el oxígeno del aire que respiras a la sangre.
C) Purificar la sangre reduciendo a cero su contenido en dióxido de carbono.
D) Transformar las moléculas de dióxido de carbono en moléculas de oxígeno."""
    ask2="""Hoy, cuando el Hemisferio Norte celebre su dia más largo, los australianos tendrán su dia más corto.
En Melbourne, Australia, el Sol saldrá las 7:36 y se pondrá a las 17:08. proporcionando 9 horas y 32
minutos de luz. Compara el dia de hoy con el dia más largo del año en el Hemisferio Sur, que será el 22
de diciembre, en el que el Sol saldrá a las 5:55 y se pondrá a las 20:42.
Proporcionando 14 horas y 47 minutos de luz.El Presidente de la Sociedad Astronómica, el señor Perry Vlahos,
dijo que la existencia de cambios de estaciones en los Hemisferios Norte y Sur estaba relacionada con
los 23 grados de inclinación del eje de la Tierra

¿Qué frase explica por qué hay día y noche en la Tierra?
A) La Tierra gira alrededor de su eje.
B) El Sol gira alrededor de su eje.
C) El eje de la Tierra está inclinado.
D) La Tierra gira alrededor del Sol."""
    ask3="""EL PAN
Un cocinero hace el pan mezclando harina, agua, sal y levadura. Una vez mezclado
todo, coloca la mezcla en un recipiente durante varias horas para que se produzca el
proceso de la fermentación. Durante la fermentación, se produce un cambio químico
en la mezcla: la levadura (un hongo unicelular) transforma el almidón y los azúcares
de la harina en dióxido de carbono y alcohol.
La fermentación hace que la mezcla se hinche. ¿Por qué se hincha?
A) Se hincha porque se produce alcohol, que se transforma en gas.
B) Se hincha porque los hongos unicelulares se reproducen dentro de ella.
C) Se hincha porque se produce un gas, el dióxido de carbono.
D) Se hincha porque la fermentación transforma el agua líquida en vapor."""
    ask4="""A Tomás le gusta mirar las estrellas. Sin embargo, no puede observarlas muy
bien por la noche porque vive en una gran ciudad.
El año pasado Tomás fue al campo y escaló una montaña desde donde
observó un gran número de estrellas que no puede ver habitualmente cuando
está en la ciudad.
¿Por qué se pueden observar más estrellas en el campo que en las ciudades donde
vive la mayoría de la gente?
A) La luna es más luminosa en las ciudades y amortigua la luz de muchas estrellas.
B) Hay más polvo que refleja la luz en el aire del campo que en el aire de la ciudad.
C) La luminosidad de las luces de la ciudad dificulta la visibilidad de las estrellas.
D) El aire de la ciudad es más caliente por el calor que emiten los coches, las
máquinas y las casas."""
    ask5="""EL CATALIZADOR
La mayor parte de los coches modernos están equipados con un catalizador. Este
catalizador hace que los gases de escape del coche sean menos perjudiciales para
las personas y para el medio ambiente.
Aproximadamente el 90 % de los gases tóxicos son transformados en gases menos
perjudiciales. Aquí podemos ver los gases que entran y salen del catalizado.
En el interior del catalizador, los gases sufren cambios. Explica qué es lo que sucede
en términos de átomos Y de moléculas.
A)Las moléculas se destruyen y los átomos se unen de nuevo para formar
moléculas diferentes.
B)El dióxido de carbono se transforma en monóxido de carbono."""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["B","A","C","C","A"]
    list_user=[]
    cont=0
    while list_user!=list_ans or (list_user!=list_ans and list_ask!=[]):
        cont+=1
        pregunta=random.choice(list_ask)
        print()
        index_ask=list_ask.index(pregunta)
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {cont}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper()
        list_user.append(answer)
        while answer!=list_ans[index_ask]:
            pregunta=random.choice(list_ask)
            print()
            index_ask=list_ask.index(pregunta)
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {cont}. Lee con atención y contesta:                                          "+ Back.RESET)
            print(f"{pregunta}\n")
            answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper()
            list_user.append(answer)
    print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
    list_ans.remove(list_ans[index_ask])
    list_ask.remove(pregunta)
    list_user=[]
    vidas+=1
    print("Felicidades. Ganaste una vida extra")
    print(" ________________________________________________________________________")
    print("|Escoge entre estas 2 opciones:                                          |")
    print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
    print("|________________________________________________________________________|")
    print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
    opc=int(input(Fore.WHITE+"Opción seleccionada:"))
    if opc==1:
        menu(vidas)
    elif opc==2:
        ciencias(vidas)
    return vidas
#CIENCIAS [CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def biologia(vidas):
    ask1="""
Las bacterias que viven en nuestra boca provocan caries dental. La caries ha sido un
problema desde el año 1700, cuando el azúcar se hizo accesible, gracias al desarrollo
de la industria de la caña de azúcar.
Hoy en día sabemos mucho sobre la caries. Por ejemplo:
• Las bacterias que provocan la caries se alimentan de azúcar.
• El azúcar se transforma en ácido.
• El ácido daña la superficie de los dientes.
• El cepillado de los dientes ayuda a prevenir la caries.

¿Cuál es el papel de las bacterias en la aparición de la caries dental?
A) Las bacterias producen esmalte.
B) Las bacterias producen azúcar.
C) Las bacterias producen minerales
D) Las bacterias producen ácido."""
    ask2="""
El tabaco se fuma en forma de cigarrillos, puros o en pipa. Ciertas investigaciones
científicas han demostrado que las enfermedades relacionadas con el tabaco matan
cada día a unas 13.500 personas en el mundo. Se predice que, para 2020, las
enfermedades relacionadas con el tabaco originarán el 12 % del total de muertes.
El humo del tabaco contiene sustancias nocivas. Las sustancias más perjudiciales son
el alquitrán, la nicotina y el monóxido de carbono.
El humo del tabaco se inhala en los pulmones. El alquitrán del humo se deposita en
los pulmones y les impide funcionar de forma adecuada.

¿Cuál de las siguientes funciones es propia del pulmón?
A) Bombear sangre oxigenada a todas las partes del cuerpo.
B) Transferir el oxígeno del aire que respiras a la sangre.
C) Purificar la sangre reduciendo a cero su contenido en dióxido de carbono.
D) Transformar las moléculas de dióxido de carbono en moléculas de oxígeno."""
    ask3="""
Algunas personas usan parches de nicotina para dejar de fumar. Los parches se
pegan a la piel y liberan nicotina a la sangre. Esto ayuda a reducir la ansiedad y
eliminar los síntomas de abstinencia cuando la gente deja de fumar.
Para estudiar la efectividad de los parches de nicotina, se escoge al azar a un grupo
de 100 fumadores que quieren dejar de fumar. Este grupo será sometido a estudio
durante seis meses. La efectividad de los parches de nicotina se determinará
contando el número de personas que no han conseguido dejar de fumar al final del
estudio.
¿Entre los siguientes, ¿cuál es el mejor diseño experimental?
A) Poner parches a todas las personas del grupo.
B) Poner parches a todo el grupo excepto a una persona que tratará de dejar de
fumar sin parches.
C) Cada persona elige si quiere llevar parche o no para dejar de fumar.
D) Se escoge al azar a una mitad del grupo que llevará parches, y la otra mitad no
los llevará.
E) Se escoge al azar a una mitad del grupo que llevará parches, y la otra mitad no
los llevará."""
    ask4="""
Puede suceder, después de una operación, que los pacientes sean incapaces de
comer y de beber, y entonces se les pone un gota a gota con suero que contiene
agua, azúcares y sales minerales. A veces también se le añaden antibióticos y
tranquilizantes.

¿Por qué los azúcares que se añaden al gota a gota son importantes para el paciente
recién operado?
A) Para evitar la deshidratación.
B) Para controlar el dolor del postoperatorio.
C) Para curar las infecciones del postoperatorio.
D) Para proporcionar la nutrición necesaria.
"""
    ask5="""
Un artículo de periódico contaba la historia de una estudiante de 22 años,
llamada Jessica, que siguió una dieta basada en el chocolate. Pretendía
mantenerse saludable, con un peso estable de 50 kilos, mientras comía
90 barritas de chocolate a la semana y prescindía del resto de la comida,
con la excepción de una «comida normal» cada cinco días. Una experta en
nutrición comentó:
“Estoy sorprendida de que alguien pueda vivir con una dieta como ésta. Las
grasas le proporcionan la energía necesaria para vivir, pero no sigue una
dieta equilibrada. En el chocolate existen algunos minerales y nutrientes,
pero no obtiene las vitaminas suficientes. Más adelante, podría sufrir serios
problemas de salud.

Los expertos en nutrición afirman que Jessica «... no obtiene las vitaminas
suficientes». Una de esas vitaminas que no contiene el chocolate es la vitamina C.
Quizás podría compensar esta carencia de vitamina C incluyendo algún alimento que
contenga un alto porcentaje de vitamina C en «la comida normal que hace cada cinco
días».
Aquí tienes una lista de tipos de alimentos,
1. Pescado.
2. Fruta.
3. Arroz.
4. Vegetales.
¿Qué dos tipos de alimentos, de los que aparecen en esta lista, recomendarías a
Jessica para que pudiera compensar la carencia de vitamina C?
A. 1 y 2
B. 1 y 3
C. 1 y 4
D. 2 y 3
E. 2 y 4
F. 3 y 4"""

    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["D","B","E","D","E"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de ciencias")
        ciencias(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    return vidas
#[CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def geologia(vidas):
    ask1="""
Hoy, cuando el Hemisferio Norte celebre su dia más largo, los australianos tendrán su dia más corto.
En Melbourne, Australia, el Sol saldrá las 7:36 y se pondrá a las 17:08. proporcionando 9 horas y 32
minutos de luz. Compara el dia de hoy con el dia más largo del año en el Hemisferio Sur, que será el 22
de diciembre, en el que el Sol saldrá a las 5:55 y se pondrá a las 20:42.
Proporcionando 14 horas y 47 minutos de luz.El Presidente de la Sociedad Astronómica, el señor Perry Vlahos,
dijo que la existencia de cambios de estaciones en los Hemisferios Norte y Sur estaba relacionada con
los 23 grados de inclinación del eje de la Tierra

¿Qué frase explica por qué hay día y noche en la Tierra?
A) La Tierra gira alrededor de su eje.
B) El Sol gira alrededor de su eje.
C) El eje de la Tierra está inclinado.
D) La Tierra gira alrededor del Sol."""
    ask2="""
El Gran Cañón está situado en un desierto de los Estados Unidos. Es un cañón muy
largo y profundo que contiene muchos estratos de rocas. En algún momento del
pasado, los movimientos de la corteza terrestre levantaron estos estratos. Hoy en día
el Gran Cañón tiene 1,6 km de profundidad en algunas zonas. El río Colorado fluye
por el fondo del cañón.

La temperatura en el Gran Cañón varía de menos de 0°C a más de 40°C C. Aunque la
zona es desértica, las grietas de las rocas a veces contienen agua. ¿De qué manera
estos cambios de temperatura y la presencia de agua en las grietas de las rocas
contribuyen a acelerar el desmenuzamiento de las rocas?
A) El agua congelada disuelve las rocas calientes.
B) El agua cementa a las rocas entre sí.
C) El hielo pule la superficie de las rocas.
D) El agua congelada se dilata en las grietas de las rocas.
"""
    ask3="""
En el estrato de caliza del Gran Cañón se encuentran muchos fósiles de animales
marinos, como almejas, peces y corales.
¿Qué sucedió hace millones de años para que aparezcan estos fósiles en este estrato?:
A) Antiguamente los habitantes transportaban alimentos marinos desde el océano a
esta área.
B) En otro tiempo, los océanos eran más violentos, y olas gigantes arrastraban
criaturas marinas hacia el interior.
C) En esa época, la zona estaba cubierta por un océano que más tarde se retiró.
D) Algunos animales marinos vivieron una vez sobre la tierra antes de emigrar al
mar."""
    ask4="""
EL TRÁNSITO DE VENUS:
El 8 de junio del 2004 fue posible ver, desde numerosos lugares de la Tierra, el paso
del planeta Venus por delante del Sol. A esto se le llama el “tránsito” de Venus, y
sucede cuando la órbita de Venus sitúa a este planeta entre el Sol y la Tierra. El
tránsito anterior de Venus sucedió en 1882, y el próximo está previsto para 2012.
Aquí vemos una foto del tránsito de Venus de 2004. Se enfocó el telescopio hacia el
Sol, y se proyectó la imagen en una hoja blanca de papel.
¿Por qué se observó el tránsito proyectando la imagen en una hoja blanca en lugar
de mirar directamente por el telescopio?
A) La luz del Sol es tan intensa que no se ve el planeta Venus.
B) El Sol es tan grande que puede verse sin necesidad de aumentos.
C) Observar el Sol a través de un telescopio puede dañar los ojos.
D) Era necesario reducir la imagen para proyectarla en una hoja.
"""
    ask5="""
De los planetas siguientes, ¿cuál puede ser observado algunas veces desde la
Tierra en tránsito delante del Sol?
A) Mercurio
B) Marte
C) Júpiter
D) Saturno"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","D","C","C","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de ciencias")
        ciencias(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    return vidas
#[CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def fisica(vidas):
    ask1="""Pedro está haciendo reparaciones en una casa vieja. Ha dejado una botella de agua,
algunos clavos metálicos y un trozo de madera dentro del maletero de su coche.
Después de que el coche ha estado tres horas al sol, la temperatura dentro del coche
llega a unos 40 ºC.
¿Qué les pasa a los objetos dentro del coche?
A) Todos tienen la misma temperatura.
B) Después de un rato el agua empieza a hervir.
C) Después de un rato los clavos están rojos incandescentes.
D) La temperatura de los clavos es mayor que la temperatura del agua."""
    ask2="""Para beber durante el día, Pedro tiene una taza con café caliente, a unos 90 ºC de
temperatura, y una taza con agua mineral fría, a unos 5 ºC de temperatura. Las
tazas son del mismo material y tamaño, y el volumen contenido en cada taza es el
mismo. Pedro deja las tazas en una habitación donde la temperatura es de unos 20
ºC.
¿Cuáles serán probablemente las temperaturas del café y del agua mineral
después de 10 minutos?
A) 70 ºC y 10 ºC.
B) 90 ºC y 5 ºC.
C) 70 ºC y 25 ºC.
D)20 ºC y 20 ºC."""
    ask3="""COMBUSTIBLES FÓSILES
Muchas centrales eléctricas queman combustibles derivados del carbono y emiten dióxido de carbono (CO),
EI CO, emitido a la atmósfera tiene un impacto negativo en el clima del planeta. Los ingenieros han usado
diferentes estrategias para reducir la cantidad de Co, que se emite a la atmósfera.
Una de esas estrategias consiste en quemar biocombustibles en lugar de combustibles fósiles. Mientras que los
combustibles fosiles proceden de organismos que muneron hace mucho tiempo, los biocombustibles proceden de plantas
que han vivido y han muerto recientemente.
Otra estrategia consiste en atrapar una parte del co. emitido por las centrales eléctricas y almacenario a cierta profundidad
bajo tierra en el mar Esta estrategia se lama captura y almacenamiento de carbonon
El uso de biocombustibles no tiene el mismo efecto en los niveles atmosféricos de CO, que el de combustibles fósiles.
¿Por qué? ¿Cuál de los siguientes enunciados lo explica mejor?:
A)Los biocombustibles no emiten CO, cuando se queman
B)Las plantas utilizadas por los biocombustibles absorben el CO. de la atmósfera a medida que crecen
C)Cuando se queman los biocombustibles toman
D)CO, de la atmósfera
E)El CO, emitido por las centrales eléctricas que utilizan biocombustibles tiene propiedades quimicas diferentes al
  CO, emitido por centrales eléctricas que utilizan combustibles fósiles"""
    ask4="""Puede suceder, después de una operación, que los pacientes sean incapaces de
comer y de beber, y entonces se les pone un gota a gota con suero que contiene
agua, azúcares y sales minerales. A veces también se le añaden antibióticos y
tranquilizantes.
Cuando la temperatura exterior es de 10℃, ¿qué diferencia hay en el consumo de
energía entre una casa con el tejado blanco y otra con el tejado negro? 
A) Hace falta más energía para calentar la casa con el techo blanco porque la luz del Sol rebota contra
él, mientras que penetra en el techo negro.
B) Hace falta más energía para calentar la casa con el techo negro porque la luz del Sol rebota contra
él, mientras que penetra en el techo blanco.
C) El techo negro refleja más la radiación solar que el blanco; por tanto, el sol calienta más la casa con
el techo blanco. """
    ask5="""¿Qué es la trayectoria de un móvil?
A. Es la línea que describe en su movimiento.
B. Es la dirección y sentido del movimiento.
C. Es el sentido del movimiento.
D. Es la dirección del movimiento."""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","A","B","A","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de ciencias")
        ciencias(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    return vidas
#[CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def quimica(vidas):
    ask1="""Barra de labios
Ingredientes:
5 g de aceite de ricino
1 g cera de abeja
1 g de cera de palmera
1 cucharada pequeña de colorante
1 gota de aroma alimentario
Instrucciones:
Caliente el aceite y las ceras al baño maría
hasta obtener una mezcla homogénea.
Añada el colorante y el aroma y mezclarlo
todo.
Aceites y ceras son sustancias que se mezclan bien entre sí. El agua no se mezcla
con los aceites, y las ceras no son solubles en agua.
Si se vuelca mucha agua dentro de la mezcla de la barra de labios cuando se está
calentando, ¿qué ocurrirá con mayor probabilidad?
A) Se producirá una mezcla más cremosa y blanda.
B) La mezcla se hará más dura.
C) La mezcla apenas cambiará.
D) Grumos grasos de la mezcla flotarán sobre el agua.
"""
    ask2="""Cuando se añade un emulsionante, éste hace que se mezclen bien los aceites y las
ceras con el agua.
¿Por qué el jabón y el agua limpian una mancha de barra de labios?
A) El agua tiene un emulsionante que permite que se mezclen el jabón y la barra de
labios.
B) El jabón actúa como un emulsionante y permite que el agua y la barra de labios
se mezclen.
C) Los emulsionantes de la barra de labios permiten que el jabón y el agua se
mezclen.
D) El jabón y la barra de labios se combinan y forman un emulsionante que se
mezcla con el agua"""
    ask3="""EL CATALIZADOR
La mayor parte de los coches modernos están equipados con un catalizador. Este
catalizador hace que los gases de escape del coche sean menos perjudiciales para
las personas y para el medio ambiente.
Aproximadamente el 90 % de los gases tóxicos son transformados en gases menos
perjudiciales. Aquí podemos ver los gases que entran y salen del catalizado.
En el interior del catalizador, los gases sufren cambios. Explica qué es lo que sucede
en términos de átomos Y de moléculas.
A)Las moléculas se destruyen y los átomos se unen de nuevo para formar
moléculas diferentes.
B)El dióxido de carbono se transforma en monóxido de carbono."""
    ask4="""EL PAN
Un cocinero hace el pan mezclando harina, agua, sal y levadura. Una vez mezclado
todo, coloca la mezcla en un recipiente durante varias horas para que se produzca el
proceso de la fermentación. Durante la fermentación, se produce un cambio químico
en la mezcla: la levadura (un hongo unicelular) transforma el almidón y los azúcares
de la harina en dióxido de carbono y alcohol.
La fermentación hace que la mezcla se hinche. ¿Por qué se hincha?
A) Se hincha porque se produce alcohol, que se transforma en gas.
B) Se hincha porque los hongos unicelulares se reproducen dentro de ella.
C) Se hincha porque se produce un gas, el dióxido de carbono.
D) Se hincha porque la fermentación transforma el agua líquida en vapor."""
    ask5="""Cuando la mezcla de pan hinchada (fermentada) se cuece en el horno, las burbujas
de gas y vapor que hay en la mezcla se dilatan.
¿Por qué se dilatan los gases y los vapores al calentarse?
A) Sus moléculas se hacen más grandes.
B) Sus moléculas se mueven más deprisa.
C) Aumenta su número de moléculas.
D) Sus moléculas entran en colisión con menos frecuencia."""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["D","B","A","C","B"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de ciencias")
        ciencias(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    return vidas
#[CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def tecnology(vidas):
    ask1="""LA ENERGÍA EÓLICA
Mucha gente piensa que la energía eólica es una fuente de energía eléctrica que
puede reemplazar las centrales térmicas de petróleo y de carbón. Las estructuras que
se observan en la foto son aerogeneradores con palas que el viento hace girar. Estos
giros producen energía eléctrica en unos generadores que son movidos por las palas
del rotor. 
A igual velocidad del viento, si los aerogeneradores están situados a mayor altitud,
giran con mayor lentitud.
Entre las razones siguientes, ¿cuál es la que mejor explica por qué las palas de los
aerogeneradores giran más despacio en los lugares situados a mayor altitud, a igual
velocidad del viento?
A) El aire es menos denso cuando aumenta la altitud.
B) La temperatura es más baja cuando aumenta la altitud.
C) La gravedad disminuye cuando aumenta la altitud.
D) Llueve más a menudo cuando aumenta la altitud.
"""
    ask2="""A Tomás le gusta mirar las estrellas. Sin embargo, no puede observarlas muy
bien por la noche porque vive en una gran ciudad.
El año pasado Tomás fue al campo y escaló una montaña desde donde
observó un gran número de estrellas que no puede ver habitualmente cuando
está en la ciudad.
¿Por qué se pueden observar más estrellas en el campo que en las ciudades donde
vive la mayoría de la gente?
A) La luna es más luminosa en las ciudades y amortigua la luz de muchas estrellas.
B) Hay más polvo que refleja la luz en el aire del campo que en el aire de la ciudad.
C) La luminosidad de las luces de la ciudad dificulta la visibilidad de las estrellas.
D) El aire de la ciudad es más caliente por el calor que emiten los coches, las
máquinas y las casas.
"""
    ask3="""Para observar estrellas de escaso brillo, Tomás utiliza un telescopio con una lente
de gran diámetro.
¿Por qué un telescopio con una lente de gran diámetro permite observar las
estrellas de escaso brillo?
A) Cuanto mayor es la lente más luz capta.
B) Cuanto mayor es la lente mayor es el aumento.
C) Las lentes grandes permiten ver más cantidad de cielo.
D) Las lentes grandes detectan los colores oscuros en las estrellas."""
    ask4="""Otra manera que tiene Peter de obtener información para mejorar la seguridad
de las carreteras es el uso de una cámara de televisión colocada sobre un poste
de 13 metros para filmar el tráfico de una carretera estrecha. Las imágenes
muestran a los investigadores cosas tales como la velocidad del tráfico, la
distancia entre los coches y qué parte de la carretera utilizan. Después de algún
tiempo se pintan líneas divisorias en la carretera. Los investigadores pueden
utilizar la cámara de televisión para observar si el tráfico es ahora diferente. ¿Es
el tráfico ahora más rápido o más lento? ¿Van los coches más o menos
distanciados entre sí que antes? ¿Los automovilistas circulan más cerca del
margen de la carretera o más cerca del centro ahora que hay líneas? Cuando
Peter conozca todo esto podrá recomendar sobre si hay que pintar o no pintar
líneas en carreteras estrechas.
Al ver la televisión, Peter ve un coche (A) que va a 45 km/h que es adelantado por
otro coche (B) que va a 60 km/h.
¿A qué velocidad le parece que va el coche B a alguien que va viajando en el coche
A?
A. 0 km/h.
B. 15 km/h.
C. 45 km/h.
D. 60 km/h.
E. 105 km/h."""
    ask5="""Un equipo de científicos británicos está desarrollando unas prendas “inteligentes" que proporcionarán
a los niños discapacitados la capacidad de “hablar”. Los niños que lleven unchaleco  hecho de un electrotejido único conectado
a un sintetizador del lenguaje serán capaces de hacerse entender golpeando simplemente el material sensible al tacto.
El material está hecho de un tejido corriente que incorpora una ingeniosa malla de fibras impregnadas en carbono que conducen la
electricidad. Cuando se presiona la tela, el conjunto de señales que pasa a través de las fibras conductoras se altera y un chip de
ordenador identifica dónde ha sido tocado el tejido. Entonces se dispara cualquier dispositivo electrónico que esté conectado a él, que podría no
ser mayor que dos cajas de cerillas. “La clave está en cómo tejemos la tela y cómo enviamos señales a través de ella. Podemos
tejerlas según los diseños de tela ya existentes con el fin de que no se vea” explica uno de los científicos.
El material puede envolver objetos, lavarse o estrujarse sin que se estropee. Los científicos afirman también que se puede fabricar en serie de
manera barata.
¿Qué instrumento del equipo del laboratorio sería el instrumento que necesitarías
para comprobar que la tela es conductora de la electricidad?
A) Un voltímetro.
B) Un fotómetro.
C) Un micrómetro.
D) Un sonómetro.
"""
    list_ask=[ask1,ask2,ask3,ask4,ask5]
    list_ans=["A","C","A","B","A"]
    for veces in range(5):
        pregunta=random.choice(list_ask)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.RED+f"Pregunta {veces+1}. Lee con atención y contesta:                                          "+ Back.RESET)
        print(f"{pregunta}\n")
        answer=input(Fore.CYAN+"ESCRIBE EL INCISO QUE CREES CORRECTO:"+ Back.RESET).upper() 
        index_ask=list_ask.index(pregunta)
        
        if answer==list_ans[index_ask]:
            print(Style.BRIGHT+Fore.GREEN+Back.MAGENTA+"Acertaste       "+ Back.RESET)
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        else:
            print(Style.BRIGHT+Fore.RED+Back.MAGENTA+"Incorrecto      "+ Back.RESET)
            vidas=vidas-1
            print(Style.BRIGHT+Fore.WHITE+Back.MAGENTA+f"Score de vidas:{vidas}"+ Back.RESET)
        list_ask.remove(pregunta)
        list_ans.remove(list_ans[index_ask])
    if vidas<=0:
        print("Lo sentimos se te acabaron los intentos.Regresarás al menú de ciencias")
        ciencias(vidas)
    elif vidas>=4:
        vidas=vidas+2
        print("Felicidades pasaste de nivel. Ganaste dos vidas adicionales")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |                                                   ")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    elif vidas<=3 and vidas>=0:
        print("Lo sentimos no pasaste el nivel.")
        print(" ________________________________________________________________________")
        print("|Escoge entre estas 2 opciones:                                          |")
        print("|1.Regresar al menú principal                                            |\n|2.Regresar al submenú                                                   |")
        print("|________________________________________________________________________|")
        print(Style.BRIGHT+Fore.RED+f"Score de vidas:{vidas}")
        opc=int(input(Fore.WHITE+"Opción seleccionada:"))
        if opc==1:
            menu(vidas)
        elif opc==2:
            ciencias(vidas)
    return vidas
#[CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def ciencias(vidas):
    print(" _______________________________________________________________________")
    print("|Menu de Opciones:                                                      |")
    print("|_______________________________________________________________________|")
    print("|1.Biología                                                             |\n|2.Geología                                                             |\n|3.Física                                                               |\n|4.Química                                                              |\n|5.Tecnología y Álgebra                                                 |\n|6.Puntos extras                                                        |\n|7.Regresar al menú principal                                           |")
    print("|_______________________________________________________________________|")
    print(Style.BRIGHT+Fore.RED+f"Score de vidas: {vidas}")
    opc=int(input(Fore.WHITE+"Selecciona la opción que más te guste:"))
    print()
    if opc==1:
        if vidas>0: 
            vidas=biologia(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            ciencias(vidas)
    elif opc==2:
        if vidas>0:
            vidas=geologia(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            ciencias(vidas)
    elif opc==3:
        if vidas>0:
            vidas=fisica(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            ciencias(vidas)
    elif opc==4:
        if vidas>0:
            vidas=quimica(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            ciencias(vidas)
    elif opc==5:
        if vidas>0:
            vidas=tecnology(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            ciencias(vidas)
    elif opc==6:
        vidas=extrasc(vidas)
    elif opc==7:
        menu(vidas)
    return vidas
#MENU LECTURA
def lectura(vidas):
    print(" ________________________________________________________________________")
    print("|Menu de Opciones:                                                       |")
    print("|________________________________________________________________________|")
    print("|1.Lectura 1                                                             |\n|2.Lectura 2                                                             |\n|3.Puntos extra                                                          |\n|4.Regresar al menú principal                                            |")
    print("|________________________________________________________________________|")
    print(Style.BRIGHT+Fore.RED+f"Score de vidas: {vidas}")
    opc=int(input(Fore.WHITE+"¿Qué te gustaria practicar?(selecciona el número): "))
    if opc==1:
        if vidas>0:
            vidas=lectora1(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            lectura(vidas)
    elif opc==2:
        if vidas>0:
            vidas=lectora2(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            lectura(vidas)
    elif opc==3:
        vidas=extrasl(vidas)
    elif opc==4:
        menu(vidas)
    else:
        print("Opción inválida")
        lectura(vidas)
    return vidas
#[CRÉDITOS:JESUS CARLOS DUEÑAS ANDALON]
def mate(vidas):
    print(" ________________________________________________________________________")
    print("|Menu de Opciones:                                                       |")
    print("|________________________________________________________________________|")
    print("|1.Aritmética y Álgebra                                                  |\n|2.Geometría                                                             |\n|3.Funciones y gráficas                                                  |\n|4.Estadística descriptiva                                               |\n|5.Combinatoria y probabilidad                                           |\n|6.Puntos extra                                                          |\n|7.Regresar al menú principal                                            |")
    print("|________________________________________________________________________|")
    print(Style.BRIGHT+Fore.RED+f"Score de vidas: {vidas}")
    opc=int(input(Fore.WHITE+"¿Qué te gustaria practicar?(selecciona el número): "))
    if opc==1:
        if vidas>0:
            vidas=aritmetica(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            #mate(vidas)
    elif opc==2:
        if vidas>0:
            vidas=geometria(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            #mate(vidas)
    elif opc==3:
        if vidas>0:
            vidas=functions(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            mate(vidas)
    elif opc==4:
        if vidas>0:
            vidas=estadistica(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            mate(vidas)
    elif opc==5:
        if vidas>0:
            vidas=probabilidad(vidas)
        else:
            print(Style.BRIGHT+Back.RED+"Los sentimos se te acabaron la vidas. No puedes continuar con esta sección"+ Back.RESET)
            mate(vidas)
    elif opc==6:
        vidas=extrasm(vidas)
    elif opc==7:
        menu(vidas)
    else:
        print("Opción inválida")
        mate(vidas)
    return vidas
#[CRÉDITOS:ISIS ATENEA OCEGUEDA MEDINA]
def menu(num_vidas):
    print(" _______________________________________________________________________")
    print("|Bienvenido a Tlatoani App joven estudiante.                            | ")
    print("|_______________________________________________________________________|")
    print("|Menu de Opciones:                                                      |")
    print("|1.Matemáticas                                                          |\n|2.Lectura                                                              |\n|3.Ciencias                                                             | \n|4.Salir                                                                |")
    print("|_______________________________________________________________________|")
    eleccion=int(input("¿Qué te gustaría aprender hoy?(selecciona el número): "))
    if eleccion==1:
        num_vidas=mate(num_vidas)
    elif eleccion==2:
        num_vidas=lectura(num_vidas)
    elif eleccion==3:
        num_vidas=ciencias(num_vidas)
    elif eleccion==4:
        pass
    else:
        print("opcion invalida")
        menu(num_vidas)
    return num_vidas
vidas=5
today=date.today()
nombre=input("Introduce tu nombre:\n")
matricula=input("Introduce tu matrícula:\n")
clave=input("Introduce tu contraseña:\n")
num_vidas= menu(vidas)

print(f"Reporte Semanal :\n")
archivo=open("reporte.txt","a")
archivo.write(f"\n*********************************************************************************************************************\nHola, ¿Qué tal? {nombre} con matrícula {matricula}. Te presentamos tu reporte actual del todo el programa.\n*El día de hoy {today}: \n* Concluiste con un total de:{num_vidas} vidas \nGracias por practicar, vuelve pronto \n*********************************************************************************************************************\n")
archivo.close()

archivo=open("reporte.txt","r")
for linea in archivo:
    print(linea)
archivo.close()





