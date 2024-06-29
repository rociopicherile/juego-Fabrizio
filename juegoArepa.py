import pgzrun
from pgzero.builtins import *

WIDTH = 1000
HEIGHT = 667

TITLE = "Arepa (Creado por: F. Tanzella)"
FPS = 60

#OBJETOS DEL JUEGO

background = Actor("canaima2")
arepa = Actor("arepa1", (500, 333))
#variable del personaje

puntaje = 0
click = 1

def draw():
    background.draw()
    arepa.draw()
    
#funcion de clicks

def on_mouse_down(button, pos):
    global puntaje
    if arepa.collidepoint(pos) and button == mouse.LEFT:
        puntaje += click
        arepa.y = 300
        animate(arepa, tween="bounce_end", duration=0.5, y=333)
        
       


pgzrun.go()

