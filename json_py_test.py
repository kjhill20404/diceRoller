import json
import time

from pprint import pprint

fightAttr = ["name","meta","Armor Class","Hit Points","Speed","STR","DEX","CON","INT","WIS","CHA","Challenge","Actions"]

class creature:
  def findCreature(creature):
    num = 0
    print(len(li))
    for item in li:
      print(li[num])
      if li[num] == creature:
        print("yo")
        return json.dumps(jsonObj[num], indent = 4, sort_keys=False,ensure_ascii=True)
      num = num + 1

  def findInfo(cratureName, key):
    cratureName = cratureName.title()
    for item in jsonObj:
      name = item.get("name")
      name = name.title()
      if name == cratureName:
        return item.get(key)


def main():

  enemy = input("What creature do you want to encounter?").title()


  if enemy.find("Fight") >= 0: #check if the word "Fight" is in the request
    print("FIGHT!!!")
    enemySplit = enemy.split(" ") #make a list out of the query using the space as the seporator

    if len(enemySplit) >2: # to check the langth of the seporated query
      enemySplit1 = str(enemySplit[1]) #set a var as the second part of the seporated list
      listIn = len(enemySplit) - 1 #check the len and subtract one from the list
      i = 2
      while i <= listIn :
        enemySplit1 = enemySplit1 + " "+ enemySplit[i]
        i = i +1
      print(enemySplit1)
      enemySplit = [0, str(enemySplit1)]
    i = 0
    listIn = len(fightAttr) - 1
    for item in fightAttr:
      value = creature.findInfo(str(enemySplit[1]), fightAttr[i])
      print(str(fightAttr[i]) + ": " + value)
      i = i +1
  else:
    print(creature.findCreature(enemy))

jsonObj = ""


def runCreature():

  with open("srd_5e_monsters.json") as jsonFile:
    global jsonObj
    jsonObj = json.load(jsonFile, strict = False)
    jsonFile.close()


  global li
  li = [item.get("name")for item in jsonObj]
  print(li)

  time.sleep(2)
  main()
