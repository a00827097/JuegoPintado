from turtle import *
from freegames import vector
from fabric.colors import yellow

def line(start, end):
    #función para crear una linea desde el primer punto seleccionada al segundo
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    #función para crear un cuadrado
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    #con un for que hace la forma del cuadrado 
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    t = turtle.Turtle()
    t.circle(50)

def rectangle(start, end):
    def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    if ((end.x - start.x)*(end.x - start.x)) > ((end.y - start.y)*(end.y - start.y)):
        for count in range(2):
            forward(end.x - start.x)
            left(90)
            forward(end.x/2 - start.x/2)
            left(90)
    elif ((end.y - start.y)*(end.y - start.y)) > ((end.x - start.x)*(end.x - start.x)):
        for count in range(2):
            forward(end.y/2 - start.y/2)
            left(90)
            forward(end.y - start.y)
            left(90)
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color ('yellow'), 'Y') #color agregado
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
