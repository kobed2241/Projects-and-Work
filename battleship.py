from Processing import *
from random import * 

"""return mouseY/100

return mouseX/100 
"""




def setUp():
    window(500, 500)
    for i in range(5):
        for j in range(5):
            fill(12,j*100,b*30)
            rect(i*100, j*100, 100, 100)
            
board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
board[randint(0,4)][randint(0,4)] = 1

setUp()



   
    
   