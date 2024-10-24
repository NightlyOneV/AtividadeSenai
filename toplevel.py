import tkinter as tk 
import time 

Main = tk.Tk()

def newWindow():
    while True:
        Secondary = tk.Toplevel()
        Secondary.title("New Window")
        
        CloseButton = tk.Button(Secondary, text="Close Window", command=Secondary.destroy)
        CloseButton.grid(row=1,column=0)
        time.sleep(1000)
    
Button = tk.Button(master=Main, text="Go to the next window.", command=newWindow)
Button.grid(row=2,column=0)

Main.mainloop()
