import random

import time

def dice(times,sides):
    timesSoFar = 0
    while timesSoFar != int(times):
        print(random.randint(1, int(sides)))
        timesSoFar = timesSoFar + 1

def requestMaker():
    request = input("What would you like to do?")

    requestSeporated = request.split(" ")#command to seporate a string into a list of eleiments

    action = requestSeporated[0]
    if action == "roll":
        a = requestSeporated[1].partition("d") #command used to seporate a sting into another list

        dice(a[0], a[2])
while(True):
    requestMaker()
