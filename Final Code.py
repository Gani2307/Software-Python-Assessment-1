import tkinter as Tk
from PIL import Image, ImageTk


global root

def Main_page():
    global root
    root=Tk.Tk()
    root.title("WORLD WAR II")
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
        root.destroy()
        Start_Quiz_Page()
        
    Start_Quiz_button = Tk.Button(root,text="Start Quiz", bg="lightgreen", font=("Arial", 30), command=Start_Quiz)
    Start_Quiz_button.place(x=100,y=400)
   

    button3 = Tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
    button3.place(x=455, y=410)

    root.mainloop()

def Overview_Page():
    Information = Tk.Tk()
    Information.title("WORLD WAR II")
    Information.geometry("800x800")
    Information.configure(background="IndianRed1")
    
    def Back_Page():
        Information.destroy()
        Main_page()

        
    Back_button = Tk.Button(Information, text = "Home", bg="lightgreen", font=("Arial", 15), command=Back_Page)
    Back_button.pack()

    Information.mainloop()

def Start_Quiz_Page():
    Question = Tk.Tk()
    Question.title("WORLD WAR II")
    Question.geometry("800x800")
    Question.configure(background="IndianRed1") 





Main_page()
