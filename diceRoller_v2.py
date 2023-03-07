import random

import time

from gui_test import infoEntry, printInfo
from json_py_test import *

prevRoll = []

options = ["roll", "last roll", "info", "create"]




class roll:
    def dice(times,sides):
        timesSoFar = 0
        while timesSoFar != int(times):
            currentRoll = random.randint(1, int(sides))
            prevRoll.append(currentRoll)
            printInfo(currentRoll)
            timesSoFar = timesSoFar + 1
        return currentRoll
    def lastRoll():
        printInfo(prevRoll)
        for e in prevRoll:
            printInfo(e)
        return prevRoll

def requestMaker():
    dReq = True
    requestSeporated = request.split(" ")#command to seporate a string into a list of eleiments

    action = requestSeporated[0]
    if action != options[0] and type(requestSeporated[0].partition("d") )== str() :
        printInfo(action)
        dReq = False
    if action == "last" and requestSeporated[1] == "roll":
        roll.lastRoll()
    elif action == options[2]:
        runCreature()
    elif action == options[3]:
        createChar()
    elif action == options[0] or dReq == True:
        printInfo(type(requestSeporated[0].partition("d") ))
        dReq = True
        if action == "roll":
            a = requestSeporated[1].partition("d") #command used to seporate a string into another list
        else:
            a = requestSeporated[0].partition("d")

        printInfo(a)
        prevRoll = []
        roll.dice(a[0], a[2])

def mainLoop(rq):
    printInfo(rq)
    run = True
    while(run == True):
        global request
        request = rq
        if request == "quit":
            run = False
        else:
            requestMaker()

mainLoop(infoEntry.getInfo())
