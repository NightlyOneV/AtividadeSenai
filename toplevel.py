import tkinter as tk 

Main = tk.Tk()

def newWindow():
    Secondary = tk.Toplevel()
    Secondary.title("New Window")
    
    CloseButton = tk.Button(Secondary, text="Close Window", command=Secondary.destroy)
    CloseButton.grid(row=1,column=0)
        
    
Button = tk.Button(master=Main, text="Go to the next window.", command=newWindow)
Button.grid(row=2,column=0)

Main.mainloop()
