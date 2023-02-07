import random

import time

from json_py_test import *

prevRoll = []

options = ["roll", "last roll", "info"]

run = True

class roll:
    def dice(times,sides):
        timesSoFar = 0
        while timesSoFar != int(times):
            currentRoll = random.randint(1, int(sides))
            prevRoll.append(currentRoll)
            print(currentRoll)
            timesSoFar = timesSoFar + 1
   
    def lastRoll():
        print(prevRoll)
        for e in prevRoll:
            print(e)

def requestMaker():
    dReq = True
    requestSeporated = request.split(" ")#command to seporate a string into a list of eleiments

    action = requestSeporated[0]
    if action != options[0] and type(requestSeporated[0].partition("d") )== str() :
        print(action)
        dReq = False
    if action == "last" and requestSeporated[1] == "roll":
        roll.lastRoll()
    elif action == options[2]:
        runCreature()

    elif action == options[0] or dReq == True:
        print(type(requestSeporated[0].partition("d") ))
        dReq = True
        if action == "roll":
            a = requestSeporated[1].partition("d") #command used to seporate a string into another list
        else:
            a = requestSeporated[0].partition("d")

        print(a)
        prevRoll = []
        roll.dice(a[0], a[2])


while(run == True):
    request = input("What would you like to do?")
    if request == "quit":
        run = False
    else:
        requestMaker()
