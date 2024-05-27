import tkinter as tk
from PIL import Image, ImageTk


# Main Page code
def Main_page():
    global homepage
    homepage=tk.Tk()
    homepage.title("WORLD WAR II")
    homepage.geometry("1000x700")
    homepage.configure(background="Khaki3")
    homepage.resizable(False, False)
    
    Title =tk.Label(homepage,text="WORLD WAR II", font=("Impact", 50), bg = "Khaki3")
    Title.pack()
    Title.place(x=490, y=50)



# Code for Button Functions
    def Overview():
        homepage.destroy()
        Open_Overview()

    def Quiz():
        homepage.destroy()
        Open_Quiz()


    # Code for Buttons
    Overview_button = tk.Button(homepage,text="Overview", bg ="lightgreen", font=("Arial", 30), command = Overview)
    Overview_button.place(x=100,y=500)
    
    Start_Quiz_button = tk.Button(homepage,text="Start Quiz", bg ="lightgreen", font=("Arial", 30), command=Quiz)
    Start_Quiz_button.place(x=100,y=400)
   

    button3 = tk.Button(homepage, text="Exit", height=3, width=15, bg ='gray20', fg ='white', command=homepage.destroy)
    button3.place(x=455, y=410)

    homepage.mainloop()
    

def Open_Quiz ():
    Question = tk.Tk()
    Question.title("WORLD WAR II")
    Question.geometry("800x800")
    Question.configure(background="IndianRed1") 
    Question.resizable(False, False)


def Open_Overview ():
    Information = tk.Tk()
    Information.title("WORLD WAR II")
    Information.geometry("800x800")
    Information.configure(background="IndianRed1")
    Information.resizable(False, False)

    def Back_Page ():
        Information.destroy()
        Main_page()

        
    Back_button = tk.Button(Information, text = "Home", bg ="lightgreen", font=("Arial", 15), command=Back_Page)
    Back_button.pack()

    Information.mainloop()



Main_page()     
