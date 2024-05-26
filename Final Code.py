import customtkinter as Tk
from PIL import Image, ImageTk


global root

def Main_page():
    root=Tk.CTk()
    root.title("WORLD WAR II")
    root.geometry("1000x700")
    root.configure(background="Khaki3")
    root.resizable(False, False)
    
    Label1 = Tk.CTkLabel(root,text="WORLD WAR II", font=("Impact", 50), bg_color= "Khaki3")
    Label1.pack()
    Label1.place(x=490, y=50)

    def Overview():
        root.destroy()
        Overview_Page()

    Overview_button = Tk.CTkButton(root,text="Overview", bg_color="lightgreen", font=("Arial", 30), command = Overview)
    Overview_button.place(x=100,y=500)
   

    def Start_Quiz():
        root.destroy()
        Start_Quiz_Page()
        
    Start_Quiz_button = Tk.CTkButton(root,text="Start Quiz", bg_color="lightgreen", font=("Arial", 30), command=Start_Quiz)
    Start_Quiz_button.place(x=100,y=400)
   

    button3 = Tk.CTkButton(root, text="Exit", height=3, width=15, bg_color='gray20', fg_color='white', command=root.destroy)
    button3.place(x=455, y=410)

    root.mainloop()

def Overview_Page():
    Information = Tk.CTk()
    Information.title("WORLD WAR II")
    Information.geometry("800x800")
    Information.configure(background="IndianRed1")
    
    def Back_Page():
        Information.destroy()
        Main_page()

        
    Back_button = Tk.CTkButton(Information, text = "Home", bg_color="lightgreen", font=("Arial", 15), command=Back_Page)
    Back_button.pack()

    Information.mainloop()

def Start_Quiz_Page():
    Question = Tk.CTk()
    Question.title("WORLD WAR II")
    Question.geometry("800x800")
    Question.configure(background="IndianRed1") 
    Question.resizable(False, False)


Main_page()
