#space invaders
#set up the screen

import turtle
import os
import math
import random

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SPace Invader")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("arial", 14, "normal"))
score_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("Blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#choose a number of enemies
number_of_enemies = 5
#create an empty list
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#create the players bullet
bullet = turtle.Turtle()
bullet.color("Yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()


bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if  bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:

    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            #move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #change enemy direction
            enemyspeed *= -1


        if enemy.xcor() < -280:
            #move all enmies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        #check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"








turtle.done()