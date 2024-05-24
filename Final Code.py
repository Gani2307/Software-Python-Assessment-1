import tkinter as Tk
from PIL import Image, ImageTk

root=Tk.Tk()
root.title("Example of a button")
root.geometry("800x800")
root.configure(background="IndianRed1")
Label1 = Tk.Label(root,text="WORLD WAR II",
               font=("Impact", 50),
               bg= "IndianRed1")
Label1.pack(pady = 20)
Label1.place(x=1000, y=100)

def Main_page():
    root=Tk.Tk()
    root.title("Example of a button")
    root.geometry("800x800")
    root.configure(background="IndianRed1")
    
    Label1 = Tk.Label(root,text="WORLD WAR II",
               font=("Impact", 50),
               bg= "IndianRed1")
    Label1.pack(pady = 20)
    Label1.place(x=1000, y=100)

    def Overview():
        root.destroy()
        Overview_Page()

    Overview_button = Tk.Button(root,text="Overview", bg="lightgreen", font=("Arial", 30), command = Overview)
    Overview_button.place(x=100,y=500)
   

    def Start_Quiz():
        Questions = Tk.Label(root)
        Questions.pack()

        
    
    Start_Quiz_button = Tk.Button(root,text="Start Quiz", bg="lightgreen", font=("Arial", 30), command=Start_Quiz)
    Start_Quiz_button.place(x=100,y=400)
   

    button3 = Tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
    button3.place(x=455, y=410)


    root.mainloop()


Information = Tk.Tk()
Information.title("Overview")
Information.geometry("800x800")

def Overview_Page():
    Information = Tk.Tk()
    Information.title("Overview")
    Information.geometry("800x800")
    
    
    
    Information.mainloop()