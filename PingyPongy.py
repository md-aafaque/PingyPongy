import turtle
import random
import time
import os
import winsound

wn = turtle.Screen()
wn.title("PingyPongy")
wn.bgcolor("#337BE6")
# the width and height can be put as user's choice
wn.setup(width = 1200, height = 700)
wn.tracer(0)

r_score = l_score = 0

# Game Starter
gs = turtle.Turtle()
gs.hideturtle()
gs.penup()
gs.goto(0,-290)
gs.color("White")
gs.write("PRESS ANY KEY TO START", align="center",font=("Arial", 24, "bold"))

# Making a box
box=turtle.Turtle()
box.width(2)
box.color("White")
box.speed(0)
box.hideturtle()
box.penup()
box.goto(500,255)
box.pendown()
for i in range(2):
	box.right(90)
	box.forward(510)
	box.right(90)
	box.forward(1000)

# Plate Right
plate_r = turtle.Turtle()
plate_r.shape("square")
plate_r.color("white")
plate_r.shapesize(stretch_wid = 3.2, stretch_len = 0.8)
plate_r.speed(0)
plate_r.penup()
plate_r.goto(460,0)

# Plate Left
plate_l = turtle.Turtle()
plate_l.shape("square")
plate_l.color("white")
plate_l.shapesize(stretch_wid = 3.2, stretch_len = 0.8)
plate_l.speed(0)
plate_l.penup()
plate_l.goto(-460, 0)

# Ball in the game
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_len=0.7,stretch_wid=0.7)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_xdir = random.uniform(1.6, 2)
ball_ydir = random.uniform(1, 2)

# Score Writing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player L : 0\t\t\tPlayer R : 0", align="center",font=("roboto", 24, "bold"))

wn.update()

def plate_r_up():
	y = plate_r.ycor()
	if y <= 218:
		plate_r.sety(y + 22)

def plate_r_down():
	y = plate_r.ycor()
	if y >= -218:
		plate_r.sety(y - 22)

def plate_l_up():
	y = plate_l.ycor()
	if y <= 218:
		plate_l.sety(y + 22)

def plate_l_down():
	y = plate_l.ycor()
	if y >= -218:
		plate_l.sety(y - 22)

wn.listen()
wn.onkeypress(plate_r_up, "p")
wn.onkeypress(plate_r_down, "l")
wn.onkeypress(plate_l_up, "w")
wn.onkeypress(plate_l_down, "s")

def run_game():
	gs.clear()
	while True:
		global ball_xdir, ball_ydir, l_score, r_score
		ball.goto(ball.xcor() + ball_xdir, ball.ycor() + ball_ydir)

		if ball.ycor() > 245:
			winsound.PlaySound("ballhit2.wav", winsound.SND_ASYNC)
			ball_ydir *= -1
		if ball.ycor() < -245:
			winsound.PlaySound("ballhit2.wav", winsound.SND_ASYNC)
			ball_ydir *= -1
		if ball.xcor() >= (plate_r.xcor() - 15) and ball.xcor() <= 447.5:
			if ball.ycor() <= (plate_r.ycor() + 39) and ball.ycor() >= (plate_r.ycor() - 39):
				winsound.PlaySound("ballhit2.wav", winsound.SND_ASYNC)
				ball_xdir = random.uniform(1.6, 2) * -1
				ball_ydir = random.uniform(1, 2) * random.choice([1, -1])
				
		if ball.xcor() <= (plate_l.xcor() + 15) and ball.xcor() >= -447.5: # (... or ball.ycor() close to plate)
			if ball.ycor() <= (plate_l.ycor() + 39) and ball.ycor() >= (plate_l.ycor() - 39):
				winsound.PlaySound("ballhit2.wav", winsound.SND_ASYNC)
				ball_xdir = random.uniform(1.6, 2)
				ball_ydir = random.uniform(1, 2) * random.choice([1, -1])

		if ball.xcor() > 493:
			winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
			ball.goto(0,0)
			ball_xdir = - random.uniform(1.6, 2)
			ball_ydir = random.uniform(1, 2) * random.choice([1, -1])
			r_score += 1
			pen.clear()
			pen.write("Player L : {}\t\t\tPlayer R : {}".format(r_score, l_score), align="center", font=("roboto", 24, "bold"))
			plate_l.goto(-460,0)
			plate_r.goto( 460,0)
			gs.write("PRESS ANY KEY TO START", align="center",font=("Arial", 24, "bold"))
			wn.update()
			break
		
		if ball.xcor() < -493:
			winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
			ball.goto(0,0)
			ball_xdir = random.uniform(1.6, 2)
			ball_ydir = random.uniform(1, 2) * random.choice([1, -1])
			l_score += 1
			pen.clear()
			pen.write("Player L : {}\t\t\tPlayer R : {}".format(r_score, l_score), align="center", font=("roboto", 24, "bold"))
			plate_l.goto(-460,0)
			plate_r.goto( 460,0)
			gs.write("PRESS ANY KEY TO START", align="center",font=("Arial", 24, "bold"))
			wn.update()
			break
		wn.update()
		# time.sleep(0.01)

wn.listen()
wn.onkeypress(run_game, " ")
turtle.done()
