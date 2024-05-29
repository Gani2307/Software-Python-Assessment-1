import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk

Questions = [
    
        "What year did World War II start?",
        "When did World War II end?",
        "Which country was not part of the Axis Powers in World War II?",
        "Who was the Prime Minister of the United Kingdom during most of World War II?",
        "Which event led to the United States entering World War II?",
        "What year did World War II start?",
    
]

Options = [
    
         ["1939", "1941", "1942", "1945"],
         ["1945", "1946", "1947", "1948"],
         ["France", "Germany", "United Kingdom", "Russia"],
         ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
         ["Attack on Pearl Harbor", "Battle of Stalingrad", "D-Day", "Bombing of Hiroshima"],
         ["1939", "1941", "1942", "1945"],
    
]

Answers = [
    "1939",
    "1945",
    "France",
    "Winston Churchill",
    "Attack on Pearl Harbor",
    "1939"
]


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
   

    Exit_button = tk.Button(homepage, text="Exit", height=3, width=15, bg ='gray20', fg ='white', command=homepage.destroy)
    Exit_button.place(x=455, y=410)

    homepage.mainloop()
    


def Open_Overview ():
    Information = tk.Tk()
    Information.title("WORLD WAR II")
    Information.geometry("1000x700")
    Information.configure(background="IndianRed1")
    Information.resizable(False, False)



    def Back_Page ():
        Information.destroy()
        Main_page()



    Back_button = tk.Button(Information, text = "Back", bg ="lightgreen", font=("Arial", 15), command=Back_Page)
    Back_button.place(x=100, y=400)

    Information.mainloop()

selected_option = ()
Answer_Entry = []


def Open_Quiz ():
    global current_question_index, score
    current_question_index = 0
    score = 0
    Quiz = tk.Tk()
    Quiz.title("WORLD WAR II")
    Quiz.geometry("1000x700")
    Quiz.configure(background="khaki3") 
    Quiz.resizable(False, False)

    Quiz_Title = tk.Label(Quiz, text="Quiz", font=("Impact", 45), bg='khaki3', padx=20, pady=10, borderwidth=2)
    Quiz_Title.pack()
    


    def Check_Answer(selected_option):
        Correct_Answer = Answers[current_question_index]
        if selected_option == Correct_Answer:
            messagebox.showinfo("Correct!", "This is the correct answer!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer is {Correct_Answer}")


    def Next_Question():
        global current_question_index
        current_question_index += 1
        if current_question_index < len(Questions):
            Get_Question()
        else:
            Final_Score()

    def Get_Question():
        global Answer_Entry
        question_label.config(text=Questions[current_question_index])
        for button in Answer_Entry:
            button.destroy()
        Answer_Entry = []
        for i, option in enumerate(Options[current_question_index]):
            Answer_Entry.append(tk.Button(Quiz, text=option, command=lambda choice=option: Check_Answer(option)))  
            Answer_Entry[i].pack()


    Correct_Answers = 0
    
    def Final_Score():
        final_screen = tk.Toplevel(Quiz)
        final_screen.title("Results")
        final_screen.geometry("500x300")
        final_screen.configure(background='navajo white')

        score_label = tk.Label(final_screen, text=f"Your score is {Correct_Answers}/{len(Questions)}", font=("Impact", 20), bg="khaki3")
        score_label.pack()

    question_label = tk.Label(Quiz, text=Questions[current_question_index], font=("Arial", 15))
    question_label.pack()

    next_button = tk.Button(Quiz, text="Next", command=Next_Question)
    next_button.place(x=100, y=300)

    Exit_button = tk.Button(Quiz, text="Exit", height=3, width=15, bg ='gray20', fg ='white', command=Quiz.destroy)
    Exit_button.place(x=455, y=410)


    Get_Question()

Main_page()     
