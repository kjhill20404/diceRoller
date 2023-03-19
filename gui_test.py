import tkinter as tk
from diceRoller_v2 import roll
questens = ["what could i do for you?"]

var= ["printFrame","rollButton","backButton","tb","addButton1","addButton2","subtractButton1","subtractButton2","timesNumLabel","timesFrame","timesLabel1","timesLabel2"]

class infoEntry:
    def getInfo(entry):
        global request
        request = entry.get()
        entry.delete(0, tk.END)
        return str(request)

def createFrame(FName,ro, colum, stick, sizeW, sizeH):
    FName = tk.Frame(window,width=sizeW, height=sizeH)
    FName.grid(row = ro, column = colum, sticky = str(stick))

class ratio:
    def hight(divNum):
        lenth = window.winfo_screenheight()
        return int(lenth / divNum)
    def width(divNum) :
        widt = window.winfo_screenwidth()
        return int(widt / divNum)
    def screen() :
        lenth = int(window.winfo_screenheight())
        widt = int(window.winfo_screenwidth())
        return str(widt) + "x" + str(lenth)

index = 0

def labelText(questen):
    global questenLabel
    questenLabel = tk.Label(text = questen)
    questenLabel.grid(row = 0, column = 0, sticky = "e",)

def TimesIncrease():
    value = int(timesNumLabel["text"])
    timesNumLabel["text"] = f"{value + 1}"

def TimesDecrease():
    value = int(timesNumLabel["text"])
    timesNumLabel["text"] = f"{value - 1}"

def sidesIncrease():
    value = int(sidesNumLabel["text"])
    sidesNumLabel["text"] = f"{value + 1}"

def sidesDecrease():
    value = int(sidesNumLabel["text"])
    sidesNumLabel["text"] = f"{value - 1}"


def addRoll():
    global sides
    sides = int(sidesNumLabel["text"])
    global times
    times = int(timesNumLabel["text"])
    global roll
    endRoll = roll.dice(times,sides)
    sidesNumLabel["text"] = 0
    timesNumLabel["text"] = 0
    tb["state"] = "normal"
    tb.insert(tk.END,str(endRoll)+"\n" )
    tb["state"] = "disabled"
    tb.pack()

def diceSection():
    diceSectionButton.grid_forget()
    labelText("how many sides would you like?")

    global sidesFrame
    sidesFrame = tk.Frame(window)
    sidesFrame.grid(row = 0, column = 1)

    global sidesNumLabel
    global sidesNum
    sidesNum = 0
    sidesNumLabel = tk.Label(master = sidesFrame, text = str(sidesNum))
    sidesNumLabel.grid(row = 0, column = 1)

    global timesLabel1
    timesLabel1 = tk.Label(text = "how many times would you like to roll the dice?")
    timesLabel1.grid(row = 1, column = 0, sticky = "e",)

    global subtractButton1
    subtractButton1 = tk.Button(master = sidesFrame, text = "-", command = sidesDecrease)
    subtractButton1.grid(row = 0, column = 0)

    global addButton1
    addButton1 = tk.Button(master = sidesFrame, text = "+", command = sidesIncrease)
    addButton1.grid(row = 0, column = 2)

    global timesFrame
    timesFrame = tk.Frame(window)
    timesFrame.grid(row = 1, column = 1)

    global timesNumLabel
    global timesNum
    timesNum = 0
    timesNumLabel = tk.Label(master = timesFrame, text = str(timesNum))
    timesNumLabel.grid(row = 0, column = 1)

    global timesLabel2
    timesLabel2 = tk.Label(text = "how many times would you like to roll the dice?")
    timesLabel2.grid(row = 1, column = 0, sticky = "e",)

    global subtractButton2
    subtractButton2 = tk.Button(master = timesFrame, text = "-", command = TimesDecrease)
    subtractButton2.grid(row = 0, column = 0)

    global addButton2
    addButton2 = tk.Button(master = timesFrame, text = "+", command = TimesIncrease)
    addButton2.grid(row = 0, column = 2)

    global printFrame
    printFrame = tk.Frame(window,width=200, height=115)
    printFrame.grid(row = 2,column = 1, sticky = "e")

    global tb
    tb = tk.Text(master = printFrame)
    tb["state"] = "disabled"
    tb.pack()

    global rollButton
    rollButton = tk.Button(master = window, text = "Roll" , command = addRoll)
    rollButton.grid(row = 3, column = 2, sticky = "e")

    global backButton
    backButton = tk.Button(master = window, text = "back" ,command = windowDestroy)
    backButton.grid(row = 3, column = 0, sticky = "e")

def windowDestroy():
    i = 0
    sidesFrame.grid_forget()
    questenLabel.grid_forget()
    sidesNumLabel.grid_forget()
    printFrame.grid_forget()
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

def TimesDecrease():
    value = int(timesNumLabel["text"])
    timesNumLabel["text"] = f"{value - 1}"

def sidesIncrease():
    value = int(sidesNumLabel["text"])
    sidesNumLabel["text"] = f"{value + 1}"

def sidesDecrease():
    value = int(sidesNumLabel["text"])
    sidesNumLabel["text"] = f"{value - 1}"


def addRoll():
    global sides
    sides = int(sidesNumLabel["text"])
    global times
    times = int(timesNumLabel["text"])
    global roll
    endRoll = roll.dice(times,sides)
    sidesNumLabel["text"] = 0
    timesNumLabel["text"] = 0
    tb["state"] = "normal"
    tb.insert(tk.END,str(endRoll)+"\n" )
    tb["state"] = "disabled"
    tb.pack()
window = tk.Tk()
window.title("quick test")


activeFrame = tk.Frame(window)
activeFrame.grid(row = 0, column = 0)

diceSectionButton = tk.Button(master = activeFrame, text = "Roll" , command = diceSection)
diceSectionButton.grid(row = 0, column = 0, sticky = "e")




window.mainloop()
