import tkinter as Tk
from PIL import Image, ImageTk

root=Tk.Tk()
root.title("Example of a button")
root.geometry("800x800")

Label1 = Tk.Label(root,text="WORLD WAR II",
               font=("Impact", 50),
               bg= "IndianRed1")
Label1.pack(pady = 20)


def Overview():
    
    Label2 = Tk.Label(root, text = "World War II was one of the most...", font=("Impact", 25), fg = "IndianRed1", bg = "IndianRed1")
    Label2.pack()
    Label1.pack_forget()
    button2.pack_forget()
    


def Start_Quiz():
    Label1.pack_forget()
    button1.pack_forget()



print("hello")


button1 = Tk.Button(root,text="Overview", bg="lightgreen", font=("Arial", 30), command=Overview)
button1.place(x=100,y=500)

button2 = Tk.Button(root,text="Start Quiz", bg="lightgreen", font=("Arial", 30), command=Start_Quiz)
button2.place(x=100,y=400)

button3 = Tk.Button(root, text="Exit", height=3, width=15, bg='gray20', fg='white', relief="raised", command=root.destroy)
button3.place(x=455, y=410)

root.configure(background="IndianRed1")
root.mainloop()
