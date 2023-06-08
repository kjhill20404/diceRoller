import tkinter as tk
from tkinter import ttk
from diceRoller_v2 import roll
from datetime import datetime


normDice = [20,12,10,8,6,4,100]

log = open('log.txt', 'a')
log.write("-------------start program-------------------")
log.write("\n")
log.close()
def addLog(textToAdd):
    log = open('log.txt', 'a')
    log.write(textToAdd)
    log.write("\n")
    log.close()

addLog(str(datetime.now()))
class infoEntry:
    def getInfo(entry):
        addLog("running infoEntry.getInfo")
        global request
        request = entry.get()
        entry.delete(0, tk.END)
        return str(request)

def createFrame(FName,ro, colum, stick, sizeW, sizeH):
    addLog("running createFrame")
    FName = tk.Frame(tab1Frame,width=sizeW, height=sizeH)
    FName.grid(row = ro, column = colum, sticky = str(stick))

class ratio:
    def hight(divNum):
        addLog("running ratio.hight")
        lenth = tab1Frame.winfo_screenheight()
        return int(lenth / divNum)
    def width(divNum) :
        addLog("running ratio.width")
        widt = tab1Frame.winfo_screenwidth()
        return int(widt / divNum)
    def screen() :
        addLog("running ratio.screen")
        lenth = int(tab1Frame.winfo_screenheight())
        widt = int(tab1Frame.winfo_screenwidth())
        return str(widt) + "x" + str(lenth)

index = 0

def oneDx(sides ,parentFrame, row1, column1, stickTo, packPlace):
    addLog("running oneDx")
    sides = int(sides)
    button = tk.Button(master = parentFrame, text = "1d" + str(sides), command = lambda: oneDxRoll(sides))
    button.grid(row = int(row1), column = int(column1), sticky = str(stickTo))
    # button.pack(side = packPlace)

def oneDxRoll(sides):
    global roll
    sides = int(sides)
    times = 1
    endRoll = roll.dice(times,sides)
    addLog(str(endRoll))
    tb["state"] = "normal"
    tb.insert(tk.END,str(endRoll)+"\n" )
    tb["state"] = "disabled"
    tb.pack()

def diceSection(parentFrame):
    addLog("running diceSection")

    global questenLabel
    questenLabel = tk.Label(master = parentFrame, text = "how many sides would you like?")
    questenLabel.grid(row = 0, column = 1, sticky = "w")

    global sidesFrame
    sidesFrame = tk.Frame(parentFrame)
    sidesFrame.grid(row = 0, column = 1)

    global sidesNumLabel
    global sidesNum
    sidesNum = 0
    sidesNumLabel = tk.Label(master = sidesFrame, text = str(sidesNum))
    sidesNumLabel.grid(row = 0, column = 1)

    global timesLabel1
    timesLabel1 = tk.Label(master = parentFrame, text = "how many times would you like to roll the dice?")
    timesLabel1.grid(row = 1, column = 1, sticky = "w",)

    global subtractButton1
    subtractButton1 = tk.Button(master = sidesFrame, text = "-", command = sidesDecrease)
    subtractButton1.grid(row = 0, column = 0)

    global addButton1
    addButton1 = tk.Button(master = sidesFrame, text = "+", command = sidesIncrease)
    addButton1.grid(row = 0, column = 2)

    global timesFrame
    timesFrame = tk.Frame(parentFrame)
    timesFrame.grid(row = 1, column = 1)

    global timesNumLabel
    global timesNum
    timesNum = 0
    timesNumLabel = tk.Label(master = timesFrame, text = str(timesNum))
    timesNumLabel.grid(row = 0, column = 1,)

    global timesLabel2
    timesLabel2 = tk.Label(text = "how many times would you like to roll the dice?")
    # timesLabel2.grid(row = 1, column = 0, sticky = "e",)

    global subtractButton2
    subtractButton2 = tk.Button(master = timesFrame, text = "-", command = TimesDecrease)
    subtractButton2.grid(row = 0, column = 0)

    global addButton2
    addButton2 = tk.Button(master = timesFrame, text = "+", command = TimesIncrease)
    addButton2.grid(row = 0, column = 2)

    global addLogFrame
    addLogFrame = tk.Frame(parentFrame,width=200, height=115)
    addLogFrame.grid(row = 2,column = 1, sticky = "e")

    global tb
    tb = tk.Text(master = addLogFrame)
    tb["state"] = "disabled"
    tb.pack()

    global rollButton
    rollButton = tk.Button(master = parentFrame, text = "Roll" , command = addRoll)
    rollButton.grid(row = 3, column = 1, sticky = "e")

    global backButton
    backButton = tk.Button(master = parentFrame, text = "back" ,command = tab1Destroy)
    backButton.grid(row = 3, column = 1, sticky = "w")

def tab1Destroy():
    addLog("runing tab1Destroy")
    i = 0
    sidesFrame.grid_forget()
    questenLabel.grid_forget()
    sidesNumLabel.grid_forget()
    addLogFrame.grid_forget()
    rollButton.grid_forget()
    backButton.grid_forget()
    tb.grid_forget()
    addButton1.grid_forget()
    addButton2.grid_forget()
    subtractButton1.grid_forget()
    subtractButton2.grid_forget()
    timesNumLabel.grid_forget()
    timesFrame.grid_forget()
    timesLabel1.grid_forget()
    timesLabel2.grid_forget()
    diceSectionButton.grid(row = 0, column = 0, sticky = "e")

def TimesIncrease():
    
    value = int(timesNumLabel["text"])
    timesNumLabel["text"] = f"{value + 1}"
    addLog("Times = " + f"{value + 1}" )

def TimesDecrease():
    value = int(timesNumLabel["text"])
    timesNumLabel["text"] = f"{value - 1}"
    addLog("Times = " + f"{value - 1}")

def sidesIncrease():
    value = int(sidesNumLabel["text"])
    sidesNumLabel["text"] = f"{value + 1}"
    addLog("Sides = " + f"{value + 1}")

def sidesDecrease():
    value = int(sidesNumLabel["text"])
    sidesNumLabel["text"] = f"{value - 1}"
    addLog("Sides = " + f"{value - 1}")


def addRoll():
    addLog("running addRoll")
    global sides
    sides = int(sidesNumLabel["text"])
    global times
    times = int(timesNumLabel["text"])
    global roll
    endRoll = roll.dice(times,sides)
    addLog(str(endRoll))
    sidesNumLabel["text"] = 0
    timesNumLabel["text"] = 0
    tb["state"] = "normal"
    tb.insert(tk.END,str(endRoll)+"\n" )
    tb["state"] = "disabled"
    tb.pack()
# window creation
window = tk.Tk()
window.title("quick test")
# for the tabbed piece
tabControl = ttk.Notebook(window) #this is to declare that we want more than one tab

tab1Frame = ttk.Frame(tabControl) #this is the frame to hold that diffrent tabs under the tabControl notebook
tab1Frame.pack()

tabControl.add(tab1Frame, text ='Tab 1') #telling tab1Frame that it is under "Tab 1" which is itself under tabControl
tabControl.pack(expand = 1, fill ="both") #placing the tabControl to the screen

paned_window1 = tk.PanedWindow(orient=tk.HORIZONTAL,bd=4,bg = "blue", relief = "raised", master = tab1Frame)
paned_window1.pack( side = tk.LEFT)

paned_window2 = tk.PanedWindow(tab1Frame, orient=tk.HORIZONTAL, bd=4, relief = "raised")
paned_window2.pack(expand = 1, fill = 'both', side = tk.RIGHT)

paned_window2.add(paned_window1)
tab1Part1 = tk.Frame(paned_window1)
tab1Part1.pack(side = "left")

paned_window1.add(tab1Part1)

diceSection(paned_window2)

buttonFrames= ttk.Frame(tab1Part1)
buttonFrames.grid(column = 0, row = 2, ipadx = 80, ipady = 100)

for i, val in enumerate(normDice):
    oneDx(normDice[i], buttonFrames, i, 0, "sw","right")

# diceSectionButton = tk.Button(master = activeFrame, text = "Roll" , command = diceSection)
# diceSectionButton.grid(row = 0, column = 0, sticky = "e")
tk.mainloop()

