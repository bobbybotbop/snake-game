import turtle
import time
from random import randint

score = 0
delay = 0.1

# Set up the screen
window = turtle.Screen()
window.setup(width = 500,height = 500)
window.bgcolor("green")
window.tracer(0)

# Head of Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#scoreboard
sb = turtle.Turtle()
sb.hideturtle()
sb.penup()
sb.color("white")
sb.goto(-240,220)
sb.pendown()
sb.write("Score: " + str(score),font = ("roboto thin",21))

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("red")
food2.penup()
food2.goto(0,-100)

segments = [] 

def go_up():
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_left():
  if head.direction != "right":
    head.direction = "left"

def go_right():
  if head.direction != "left":
    head.direction = "right"

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  
  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)
  
  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)

window.onkey(go_up, "Up")
window.onkey(go_left, "Left")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.listen()

while True:
  window.update()
  
  sb.clear()
  sb.write("Score: " + str(score),font = ("roboto thin",21))

  #Eating Food
  if head.distance(food) < 20:
    x = randint(-240,240)
    y = randint(-240,240)
    while(x % 20 != 0):
      x = randint(-240,240)
    while(y % 20 != 0):
      y = randint(-240,240)
    food.goto(x,y)
    delay -= 0.005

    #Add a segment onto Snake
    newSegment = turtle.Turtle()
    newSegment.speed(0)
    newSegment.shape("square")
    newSegment.color("black","grey")
    newSegment.penup()
    segments.append(newSegment)

    score += 1

    #eat2
  if head.distance(food2) < 20:
    x = randint(-240,240)
    y = randint(-240,240)
    while(x % 20 != 0):
      x = randint(-240,240)
    while(y % 20 != 0):
      y = randint(-240,240)
    food2.goto(x,y)
    delay -= 0.005

    #Add a segment onto Snake
    newSegment = turtle.Turtle()
    newSegment.speed(0)
    newSegment.shape("square")
    newSegment.color("black","grey")
    newSegment.penup()
    segments.append(newSegment)

    score += 1
    
  #Move segments in reverse order
  for index in range(len(segments)-1, 0,-1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)
  
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)
  
  move()

  #Body Collision
  for piece in segments:
    if piece.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"
      score = 0
      for piece in segments:
        piece.goto(1000,1000)
      
      del segments [:]

      delay = 0.1


    if head.xcor()>250 or head.xcor()<-250 or head.ycor()>250 or head.ycor()<-250:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"
      score = 0
      
  time.sleep(delay)

