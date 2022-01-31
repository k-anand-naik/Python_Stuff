import turtle
import time

tim = turtle.Turtle()
tim.color('green')
tim.pensize(5)
tim.shape('turtle')

tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()
tim.color('red')
tim.forward(200)
tim.speed(1)

dave = turtle.Turtle()
dave.color('purple')
dave.pensize(10)
dave.backward(200)

time.sleep(2)