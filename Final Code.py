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
    homepage.configure(background="#1F2833")
    homepage.resizable(False, False)
    
    Title =tk.Label(homepage,text="WORLD WAR II", font=("Impact", 50), bg = "#1F2833")
    Title.config(fg="#66FCF1")
    Title.pack()
    Title.place(x=310, y=50)



# Code for Button Functions
    def Overview():
        homepage.destroy()
        Open_Overview()

    def Quiz():
        homepage.destroy()
        Open_Quiz()


    # Code for Buttons
    Overview_button = tk.Button(homepage,text="Overview", bg ="IndianRed1", font=("Arial", 15), height = 1, width = 7, command = Overview)
    Overview_button.place(x=50,y=553)
    
    Start_Quiz_button = tk.Button(homepage,text="Start Quiz", bg ="lightgreen", font=("Arial", 15), height = 1, width = 8, command=Quiz)
    Start_Quiz_button.place(x=800,y=550)
   

    Exit_button = tk.Button(homepage, text="Exit", bg ='goldenrod2', fg ='black',font=("Arial", 15), width = 7, height = 1, command=homepage.destroy)
    Exit_button.place(x=425, y=550)

    homepage.mainloop()
    

# OVERVIEW PAGE
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



# START THE QUIZ 
Answer_Entry = []
current_question_index = 0
score = 0

def Back_to_Home():
     Open_Quiz.destroy()
     Main_page()

def Check_Answer(selected_option):
        global score
        correct_answer = Answers[current_question_index]
        selected_answer = Options[current_question_index][selected_option]
        if selected_answer == correct_answer:
            messagebox.showinfo("Correct!", "This is the correct answer!")
            score += 1
            Next_Question()
        else:
            messagebox.showerror("Incorrect", f"The correct answer is {correct_answer}")
            Next_Question()

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
        Answer_Entry.append(tk.Button(quiz_frame, text=option, command=lambda selected_option=i: Check_Answer(selected_option)))
        Answer_Entry[i].pack()


        Correct_Answers = 0
    
def Final_Score():
    Score_Page = tk.Toplevel(quiz)
    Score_Page.title("Results")
    Score_Page.geometry("500x300")
    Score_Page.configure(background='navajo white')

    Score = tk.Label(Score_Page, text=f"Your score is {score}/{len(Questions)}", font=("Impact", 20), bg="khaki3")
    Score.pack()

def Open_Quiz():
    global quiz, quiz_frame, question_label, Answer_Entry
    quiz = tk.Tk()
    quiz.title("WORLD WAR II")
    quiz.geometry("1200x700+100+100")
    
    quiz.configure(background="khaki3")
    quiz.resizable(False, False)

    quiz_title = tk.Label(quiz, text="Quiz", font=("Impact", 45), bg='khaki3', padx=20, pady=10, borderwidth=2)
    quiz_title.pack()

    quiz_frame = tk.Frame(quiz, bg="khaki3")
    quiz_frame.pack(pady=20)

    question_label = tk.Label(quiz_frame, text=Questions[current_question_index], font=("Arial", 15))
    question_label.pack()

    Exit_button = tk.Button(quiz, text="Exit", height=3, width=15, bg ='gray20', fg ='white', command=quiz.destroy)
    Exit_button.place(x=455, y=410)

    Main_Menu_button = tk.Button(quiz, text="Main Menu", height=3, width=15, bg ='gray20', fg ='white', command=Back_to_Home)
    Main_Menu_button.place(x=355, y=410)

    Get_Question()

    quiz.mainloop()

    Quiz_Title = tk.Label(quiz, text="Quiz", font=("Impact", 45), bg='khaki3', padx=20, pady=10, borderwidth=2)
    Quiz_Title.pack()
    
    

    question_label = tk.Label(quiz, text=Questions[current_question_index], font=("Arial", 15))
    question_label.pack()

    Exit_button = tk.Button(quiz, text="Exit", height=3, width=15, bg ='gray20', fg ='white', command=quiz.destroy)
    Exit_button.place(x=455, y=410)



    Get_Question()

Main_page()     
