from random import *
from Myro import *

houseList = ["apartment", "whiteHouse", "under a bridge", "cardboad tent"] 
hlResponse = raw_input("where do you live? ")
houseList.append(hlResponse)

foodList = ["banana", "whole pickle", "cucumber", "eggplant"]
flResponse = raw_input("what healthy food do you like to consume? ")
foodList.append(flResponse)

staffList = ["Oliver", "Stephen", "Austin", "De Andre"]
slResponse = raw_input("Who's the best teacher? ")
staffList.append(slResponse) 


print("You currently live...", choice(houseList))
print("While chewing on a...", choice(foodList))
print("While admiring the man of the house,...", choice(staffList))




