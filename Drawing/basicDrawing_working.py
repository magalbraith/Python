from graphics import *
import random

# set up classes for each ball (as below)
# assign each ball with a position and then set up a for loop for next number in the list. the color of this ball is determined
#by the number the ball must be set up to be in one of the six groups ie <39 etc.  see below.
#one the area where the ball is put then the ball must be placed next to the last ball in that group which will be double the diameter of
#the previous ball.


# Create a drawing window by importing GraphWin

window = GraphWin("Results", 600, 600)
myImage = Image(Point(100,100),"justin_bieber.gif")
myImage.draw(window)

#window_background_image = src( "fruit_machine.jpg")
#Read in and print out the data in the data file
datafile = open("data.txt",'r')

#yellow circle for <39

for line in datafile:
    number = float(line)
    print(number)
    if(number <= 39):
        xpos = random.randint(0,int(200-number))
        ypos = random.randint(0,int(300-number))
        ball = Circle(Point(xpos,ypos),number) #write this circle at first number
        ball.setOutline('orange')
        ball.setFill(color_rgb(255,255,0))
        ball.draw(window)
        text = Text(Point(60,50), 'The Lowest Scores!!')
        text.draw(window)
        
 #orange circle for <49       

    if(number <= 49):
        xpos = random.randint(200,int(400-number))
        ypos = random.randint(0,int(300-number))
        ball = Circle(Point(xpos,ypos),number)
        ball.setOutline('green')
        ball.setFill(color_rgb(255,215,0))
        ball.draw(window)
        
 #blue circle for <59       

    if(number <= 59):
        xpos = random.randint(400,int(600-number))
        ypos = random.randint(0,int(300-number))
        ball = Circle(Point(xpos,ypos),number)
        ball.setOutline('red')
        ball.setFill(color_rgb(100,149,237))
        ball.draw(window)

 #green circle for <69       

    if(number <= 69):
        xpos = random.randint(0,int(200-number))
        ypos = random.randint(300,int(600-number))
        ball = Circle(Point(xpos,ypos),number)
        ball.setOutline('yellow')
        ball.setFill(color_rgb(0,250,154))
        ball.draw(window)

#violet circle for <79       

    if(number <= 79):
        xpos = random.randint(200,int(400-number))
        ypos = random.randint(200,int(600-number))
        ball = Circle(Point(xpos,ypos),number)
        ball.setOutline('yellow')
        ball.setFill(color_rgb(148,0,211))
        ball.draw(window)

#red circle for <79       

    if(number <= 79):
        xpos = random.randint(400,int(600-number))
        ypos = random.randint(400,int(600-number))
        ball = Circle(Point(xpos,ypos),number)
        ball.setOutline('blue')
        ball.setFill(color_rgb(253,11,0))
        ball.draw(window)

        text = Text(Point(500,400), 'Highest Scores!!')
        text.draw(window)


"""
  

#class yellowBall():
    #yellowBall =Circle(Point(10,10),number) #write this circle at first number
    #then write the next until you reach 39
    #yellowBall.setFill(color_rgb(255,255,0))
    #yellowBall.draw(window)
    #place all the circles representing numbers =< 39
    # in the square x =< 200
    # in the square y =< 0, -300
"""

#class orangeBall ():
    #orangeBall =Circle(Point(20,20),float(number))
    #orangeBall.setFill(color_rgb(255,215,0))
    #orangeBall.draw(window)
    #place =<49
    # in the square x => 200 & <400
    # in the square y =< -300
    
#class blueBall():
    #blueBall =Circle(Point(30,30),float(number))
    #blueBall.setFill(color_rgb(100,149,237))
    #blueBall.draw(window)
    #place =<59
    
#class greenBall():
    #greenBall =Circle(Point(40,40),float(number))
    #greenBall.setFill(color_rgb(0,250,154))
    #greenBall.draw(window)
    #place =<69
    
#class violetBall():
    #violetBall =Circle(Point(50,50),float(number))
    #violetBall.setFill(color_rgb(148,0,211))
    #violetBall.draw(window)
    #place =<79
    
#def redBall ():
    #redBall =Circle(Point(60,60),float(number))
    #redBall.setFill(color_rgb(253,11,0))
    #redBall.draw(window)
    #place =>79
    
#print (yellowBall)
#print (orangeBall)
#print (blueBall)
#print (greenBall)
#print (violetBall)  
#print (redBall) 


#for number in datafile:
#    print(number)
#    ball = Circle(Point(100,100), float(number))
#    ball.setFill(color_rgb(255,255,0))
#    ball.draw(window)

#box = Rectangle(Point(200,50),Point(250,150))
#box.setOutline(color_rgb(255,0,0))
#box.draw(window)

#line = Line(Point(200,200),Point(250,280))
#line.setWidth(4)
#line.draw(window)

#text = Text(Point(50,200),"Hello")
#text.draw(window)

# Waits until the mouse is clicked before closing the window
#window.getMouse()
