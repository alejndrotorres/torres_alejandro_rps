# This file was created by: Alejandro Torres
# Thank you and props to Jaden Parrish for the help

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = -300
rock_pos_y = 0

# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)

# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# add the paper image as a shape
screen.addshape(paper_image)
# attach the paper_image to the paper_instance
paper_instance.shape(paper_image)
# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for paper position
paper_pos_x = 0
paper_pos_y = 0

# set the position of the paper_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the paper image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
# add the scissors image as a shape
screen.addshape(scissors_image)
# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for scissors position
scissors_pos_x = 300
scissors_pos_y = 0
# set the position of the scissors_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

# function that passes through wn onlick
# ROCK HITBOX
def someFunction(x, y):
    # print("window geometry " + str(cv.winfo_geometry()))
    # screen.setup(WIDTH,HEIGHT,0,0)
    global playerchoice
    if x > -430 and y > -144 and x < -170 and y < 144: # rocks position restrictions to register as a hitbox
        playerchoice = "rock"
        print("player chose " + playerchoice)
        t.penup()
        t.goto(x, y)
        text.goto(x, y)
        text.write("rock!", False, "left", ("Arial", 24, "normal"))
        # turtle.write(str(x)+","+str(y))
        # print(str(x)+","+str(y))
        run()
    elif x > -130 and y > -105 and x < 130 and y < 106: # papers position restrictions to register as a hitbox
        playerchoice = "paper"
        print("player chose " + playerchoice)
        t.penup()
        t.goto(x, y)
        text.goto(x, y)
        text.write("paper!", False, "left", ("Arial", 24, "normal"))
        # turtle.write(str(x)+","+str(y))
        # print(str(x)+","+str(y))
        run()
    elif x > 172 and y > -85 and x < 430 and y < 85: # scissors position restrictions to register as a hitbox
        playerchoice = "scissors"
        print("player chose " + playerchoice)
        t.penup()
        t.goto(x, y)
        text.goto(x, y)
        text.write("scissors!", False, "left", ("Arial", 24, "normal"))
        # turtle.write(str(x)+","+str(y))
        # print(str(x)+","+str(y))
        run()

from random import randint
# imports randint from random
options = ["rock", "paper", "scissors"]
# creates a list of options the player and cpu can choose from

def run (): # defining function of all possible outcomes that lead to winning, losing, or drawing
    print("I see that player chose " + playerchoice) #terminal text
    cpuchoice = options[randint(0,len(options)-1)] #computer is picking a random choice
    print ("the cpu chose " + str(cpuchoice)) #terminal text
    if playerchoice == "rock": #if player chooses rock then... 
        paper_instance.hideturtle() #if player chooses rock then the image of paper will dissapear
        scissors_instance.hideturtle() #if player chooses rock then the image of paper will dissapear
        if cpuchoice == "rock": # if random choice from cpu is rock it will print this
            t.goto (-320,150) #coordinates of text
            t.write ("It's a tie") #text that displays when cpu chooses rock
            t.goto (-320, 160) #coordinates of text
            t.write ("CPU chose rock") #text will display above players choice
        elif cpuchoice == "paper": # if cpu chooses paper then...
            t.goto(-320,150) #coordinates of text
            t.write ("You lose") # text that displays when cpu chooses paper
            t.goto (-320, 160) #coordinates of text
            t.write ("CPU chose paper") #text that displays when cpu chooses paper
        elif cpuchoice == "scissors": #if cpu chooses scissors then...
            t.goto(-320,150) #coordinates of text
            t.write ("You win") #text that displays when cpu chooses scissors
            t.goto (-320,160) #coordinates of text
            t.write ("CPU chose scissors") #text that displays when cpu chooses scissors
    elif playerchoice == "paper": #if player chooses paper then...
        rock_instance.hideturtle() #if player chooses paper then the image of rock will dissapear
        scissors_instance.hideturtle() #if player chooses paper then the image of scissors will dissapear
        if cpuchoice == "paper": #if cpu chooses paper then...
            t.goto(-20,120) #coordinates of text
            t.write ("It's a tie") #text that displays when cpu chooses paper
            t.goto(-20,130) #coordinates of text
            t.write ("CPU chose paper") #text that displays when cpu chooses paper
        elif cpuchoice == "scissors": #if cpu chooses scissors then...
            t.goto(-20,120) #coordinates of text
            t.write ("You lose") #text that displays when cpu chooses scissors
            t.goto(-20,130) #coordinates of text
            t.write("CPU chose scissors") #text that displays when cpu chooses scissors
        elif cpuchoice == "rock": #if cpu chooses rock then...
             t.goto(-20,120) #coordinates of text
             t.write ("You win") #text that displays when cpu chooses rock
             t.goto(-20,130) #coordinates of text
             t.write ("CPU chose rock") #text that displays when cpu chooses rock
    elif playerchoice == "scissors": #if player chooses scissors then...
        rock_instance.hideturtle() #if player chooses scissors then the image of rock will dissapear
        paper_instance.hideturtle() #if player chooses scissors then the image of paper will dissapear
        if cpuchoice == "scissors": #if cpu chooses scissors then...
            t.goto(280,100) #coordinates of text
            t.write ("Its a tie") #text that displays when cpu chooses scissors
            t.goto(280,110) #coordinates of text
            t.write ("CPU chose scissors") #text that displays when cpu chooses scissors
        elif cpuchoice == "rock": #if cpu chooses rock then...
            t.goto(280,100) #coordinates of text
            t.write ("You lose") #text that displays when cpu chooses rock
            t.goto(280,110) #coordinates of text
            t.write("CPU chose rock") #text that displays when cpu chooses rock
        elif cpuchoice == "paper": #if cpu chooses paper then...
            t.goto(280,100) #coordinates of text
            t.write ("You win") #text that displays when cpu chooses paper
            t.goto(280,110) #coordinates of text
            t.write("CPU chose paper") #text that displays when cpu chooses paper
    else: 
        print ("that's not a valid input, try again") #redirect person to make a choice if they did not choose rock, paper, or scissors
        run ()

# run function
# onclick action runs function on turtle window using x and y coordinates
# https://docs.python.org/3/library/turtle.html#turtle.onclick
def mouse_pos(x,y): #function that registers a choice when mouse clicks on either rock, paper, or scissors 
    global playerchoice
    if str(collide(x,y, rock_instance, rock_w, rock_h)) == "True":
        playerchoice = "rock"
    elif str(collide(x,y, paper_instance, paper_w, paper_h)) == "True":
        playerchoice = "paper"
    elif str(collide(x,y, scissors_instance, scissors_w, scissors_h)) == "True":
        playerchoice = "scissors"

screen.onclick(someFunction)
# runs mainloop for Turtle - required to be last
screen.mainloop()