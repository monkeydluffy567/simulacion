from turtle import *
import random
home()


# Abstraemos el límite recursivo en esta constante para entender mejor el
# código
MAX_DEPTH = 6
r = lambda: random.randint(0,255)#para producir numeros random que serviran para definir un color random
bgcolor("black")
def hoja(profundidad=0,angulo=0):
    if profundidad > MAX_DEPTH:
        return
    left(angulo)
    color2='#%02X%02X%02X' % (r(),r(),r())
    color(color2)
    longitud = 100 * (2/3)**profundidad

    forward(longitud)
    left(60)

    # Primera llamada recursiva, ramas izquierdas
    hoja(profundidad+1)

    # Asumimos que la llamada recursiva va a terminar al principio de la línea
    # recién dibujada
    right(120)

    # ¡Dos llamadas recursivas en la mimsa función! Ramas derechas
    hoja(profundidad+1)

    right(120) # completamos una vuelta de 360 grados hacia la derecha
    forward(longitud) # regresamos lo mismo que avanzamos
    left(180) # damos media vuelta


home()
hoja() 
hoja(0,120)
hoja(0,120)
exitonclick()