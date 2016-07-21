from random import *

"""
def setup():
  size(500,500) 
  background(255,255,255)


def draw():
  rsize = 10
  rcolor = randrange(0,255)
  bcolor = randrange(0,255)
  gcolor = randrange(0,255)
  mycolor = color(rcolor, bcolor, gcolor)
  noStroke()
  fill(mycolor)
  

  for i in range(100): 
      ellipse(mouseX , mouseY , rsize, rsize)
      ellipse(mouseX + 20 , mouseY , rsize, rsize)
      ellipse(mouseX - 20 , mouseY , rsize, rsize)
      ellipse(mouseX , mouseY + 20   , rsize, rsize)
      ellipse(mouseX , mouseY - 20, rsize, rsize)
      """
      
def setup():
  size(1000,1000) 
  background(31)
  
  #red color 
  fill(255,0,0)
  rect(0, 0, 100, 100)
  
  #blue color
  fill(0,0,255)
  rect(100, 0, 100, 100)
  
  #green color
  fill(0,255,0)
  rect(200,0,100,100)
  
  #black color
  fill(0,0,0)
  rect(300,0,100,100)
  
  
  
  
  
  
def draw():
    global ColorMode 
    
    colorMode = 0;
    if mouseY < 100:
        if mouseX < 100 and mousePressed:
            ColorMode = 1
        elif mouseX < 200 and mousePressed:
            ColorMode = 2
        elif mouseX < 300 and mousePressed:
            ColorMode = 3
        elif mouseX
            
    elif mouseY > 100:
        if mousePressed and ColorMode == 1: 
            fill(255,0,0) 
            stroke(180, 180, 0)
            ellipse(mouseX, mouseY, 10, 10) 
        if mousePressed and ColorMode == 2:
            fill(0,0,255) 
            stroke(180,180,0) 
            ellipse(mouseX,mouseY,10,10)
        if mousePressed and ColorMode == 3:
            fill(0,255,0)
            stroke(180,180,0)
            ellipse(mouseX,mouseY,10,10)
    
            
  

  
    

  