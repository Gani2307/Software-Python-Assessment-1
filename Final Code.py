import tkinter as tk
from PIL import Image, ImageTk

current_score_index = 0
score = 0

Questions = [

    {
        "Question": "What year did World War II start?",
        "options": ["1939", "1941", "1942", "1945"],
        "answer": "1939"
    },
    {
        "Question": "When did World War II end?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1945"
    },
    {
        "Question": "Which country was not part of the Axis Powers in World War II?",
        "options": ["Germany", "Japan", "Italy", "France"],
        "answer": "France"
    },
    {
        "question": "Who was the Prime Minister of the United Kingdom during most of World War II?",
        "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Stanley Baldwin"],
        "answer": "Winston Churchill"
    },
    {
        "Question": "Which event led to the United States entering World War II?",
        "options": ["Attack on Pearl Harbor", "Battle of Stalingrad", "D-Day", "Bombing of Hiroshima"],
        "answer": "Attack on Pearl Harbor"
    },
    {
        "Question": "What year did World War II start?",
        "options": ["1939", "1941", "1942", "1945"],
        "answer": "1939"
    },
    {
        "Question": "When did World War II end?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1945"
    }
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
   

    button3 = tk.Button(homepage, text="Exit", height=3, width=15, bg ='gray20', fg ='white', command=homepage.destroy)
    button3.place(x=455, y=410)

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

selected_option = None



def Open_Quiz ():
    global current_score_index, score
    current_score_index = 0
    score = 0
    Question = tk.Tk()
    Question.title("WORLD WAR II")
    Question.geometry("1000x700")
    Question.configure(background="IndianRed1") 
    Question.resizable(False, False)

    def Check_Answer(selected_option):
        global current_question_index, score
        print(current_question_index)
        Correct_Answer = Questions[current_question_index]["Answer"]

    def Back_Page ():
        Question.destroy()
        Main_page()

    Back_button = tk.Button(Question, text = "Back", bg ="lightgreen", font=("Arial", 15), command=Back_Page)
    Back_button.pack()

 





Main_page()     
