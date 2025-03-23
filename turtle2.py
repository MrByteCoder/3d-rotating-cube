import turtle
import math
import time


screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0) 


pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color("cyan")
pen.hideturtle()


vertices = [
    [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],  
    [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]  
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  
    (4, 5), (5, 6), (6, 7), (7, 4), 
    (0, 4), (1, 5), (2, 6), (3, 7)  
]

angle = 0

def rotate_x(point, angle):
    """Rotate a point around the X-axis"""
    rad = math.radians(angle)
    y = point[1] * math.cos(rad) - point[2] * math.sin(rad)
    z = point[1] * math.sin(rad) + point[2] * math.cos(rad)
    return (point[0], y, z)

def rotate_y(point, angle):
    """Rotate a point around the Y-axis"""
    rad = math.radians(angle)
    x = point[0] * math.cos(rad) + point[2] * math.sin(rad)
    z = -point[0] * math.sin(rad) + point[2] * math.cos(rad)
    return (x, point[1], z)

def project_2d(point):
    """Project 3D points to 2D screen"""
    factor = 200 / (point[2] + 200)  
    x = point[0] * factor
    y = point[1] * factor
    return (x, y)

def draw_cube():
    """Draw the rotating 3D cube"""
    global angle
    pen.clear()

    transformed = [rotate_x(p, angle) for p in vertices]
    transformed = [rotate_y(p, angle) for p in transformed]
    projected = [project_2d(p) for p in transformed]

    for edge in edges:
        p1 = projected[edge[0]]
        p2 = projected[edge[1]]
        pen.penup()
        pen.goto(p1)
        pen.pendown()
        pen.goto(p2)

    screen.update()
    angle += 2  


while True:
    draw_cube()
    time.sleep(0.05)