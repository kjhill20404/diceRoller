import tkinter as tk

questens = ["what could i do for you?"]

class infoEntry:
    def getInfo():
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
    questenLabel = tk.Label(text = questen)
    questenLabel.grid(row = 0, column = 0, sticky = "e",)



def printInfo(event):
    global request
    request = entry.get()
    entry.delete(0, tk.END)
    tb["state"] = "normal"
    # tb.delete("1.0", tk.END)
    tb.insert(tk.END,request+"\n" )
    tb["state"] = "disabled"
    # label2.grid(row = 1, column = 0, sticky = "e",)
    tb.pack()



window = tk.Tk()
window.title("quick test")
# window.geometry("700x500")

labelText("what could I do for you?")

entry = tk.Entry(width=20)
entry.grid(row = 0, column = 1)


printFrame = tk.Frame(window,width=375, height=115)
printFrame.grid(row = 1,column = 1, sticky = "e")
tb = tk.Text(master = printFrame)
tb["state"] = "disabled"
tb.pack()


window.bind("<Return>", printInfo)
print(infoEntry.getInfo())


window.mainloop()
