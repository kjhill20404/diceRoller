import tkinter as tk                     
from tkinter import ttk 
  
  
root = tk.Tk() 
root.title("Tab Widget") 
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='Tab 1') 
tabControl.pack(expand = 1, fill ="both") 

paned_window1 = tk.PanedWindow(tab1, orient = tk.VERTICAL, bg='red', bd=10)
paned_window1.pack(expand=True, fill='both')


label = tk.Label(text='See it is possible')
paned_window1.add(label)


root.mainloop()  
 