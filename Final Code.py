import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk

Questions = [
    
        "1. What year did World War II start?",
        "2. When did World War II end?",
        "3. Which country was not part of the Axis Powers in World War II?",
        "4. Who was the Prime Minister of the United Kingdom during most of World War II?",
        "5. Did the United States enter World War II before or after the attack on Pearl Harbor",
        "6. Did Germany invade Poland in 1939?",
        "7. Was the Battle of Britain primarily fought in the air?",
        "8. Which Allied forces landed in Normandy on D-Day?",
        "9. What was the outcome of the use of atomic bombs in Japan?",
        "10. Japan had been at war for four years prior to the attack on Pearl Harbor with which country?",
        "11. The Japanese emperor during World War II was...?",
        "12.  What was the name of the American effort to build an atomic bomb?",
        "13. How many aircraft carriers did the Japanese destroy during their attack on Pearl Harbor?",
        "14. What was the code name of the German invasion of the Soviet Union?",
        "15. Which of the following is NOT a Winston Churchill speech?"
        
]
Options = [
    
         ["1942", "1941", "1939", "1945"],
         ["1946", "1945", "1947", "1948"],
         ["United Kingdom", "Germany", "France", "Russia"],
         ["Stanley Baldwin", "Neville Chamberlain", "Clement Attlee", "Winston Churchill"],
         ["Before", "After"],
         ["True", "False"],
         ["Aerial bombings", "Naval Engagements", "Ground Battle", "Trench Warfare"],
         ["British and French", "British and Canadian", "American and British", "American and Canadian"],
         ["Japan surrendered immediately", "Japan launched a counterattack", "Japan sought a conditional surrender", "Japan ignored the bombs"],
         ["China", "Indonesia", "Cambodia"],
         ["Hirohito", "Hiroshima", "Hiromatsu", "Tojo"],
         ["The Baltimore Project", "The Chicago Project", "The Manhattan Project", "The Philadelphia Project"],
         ["1", "6", "4", "10"],
         ["Operation Barbarossa", "Operation Overlord", "Operation Sea Lion", "Operation Torch"],
         ["I have nothing to offer but blood, toil, tears and sweat", "This was their finest hour", "We have nothing to fear but fear itself", "We shall fight on the beaches"]
    
]

Answers = [
    "1939",
    "1945",
    "France",
    "Winston Churchill",
    "After",
    "True",
    "Aerial bombings",
    "American and British",
    "Japan surrendered immediately",
    "China",
    "Hirohito",
    "The Manhattan Project",
    "6",
    "Operation Barbarossa",
    "We have nothing to fear but fear itself"
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
    Overview_button = tk.Button(homepage,text="Overview", bg ="#1F2833", font=("Arial", 15), fg = "white", height = 1, width = 7, command = Overview)
    Overview_button.config(fg = "#66FCF1")
    Overview_button.place(x=50,y=553)
    
    Start_Quiz_button = tk.Button(homepage,text="Start Quiz", bg ="#1F2833", font=("Arial", 15), height = 1, width = 8, command=Quiz)
    Start_Quiz_button.config(fg = "#66FCF1")
    Start_Quiz_button.place(x=800,y=550)
   

    Exit_button = tk.Button(homepage, text="Exit", bg ='#1F2833',font=("Arial", 15), width = 7, height = 1, command=homepage.destroy)
    Exit_button.config(fg = "#66FCF1")
    Exit_button.place(x=425, y=550)

    homepage.mainloop()
    

# OVERVIEW PAGE
def Open_Overview ():
    global Information
    Information = tk.Tk()
    Information.title("WORLD WAR II")
    Information.geometry("1000x700")
    Information.configure(background="#1F2833")
    Information.resizable(False, False)

    Overview_title =tk.Label(Information,text="OVERVIEW", font=("Impact", 50), bg = "#1F2833")
    Overview_title.config(fg="#66FCF1")
    Overview_title.place(x=340, y=50)

    Overview_Information = tk.Label(Information, text = "After Germany invaded Poland in 1939, the world saw the outbreak of World War II, which lasted until 1945. \n During most of the war, Winston Churchill served as Prime Minister of the United Kingdom, encouraging the \n country with his motivational speeches. The devastation caused by the 1941  attack on Pearl Harbor led the \n United States to ally with the Allies in opposition to the Axis Powers and enter the war. The Royal Air Force fought \n the Luftwaffe in the Battle of Britain, mostly from the air. An important moment in European history was the landing \n of Allied forces in Normandy  on D-Day in 1944. Japan's quick surrender and the end of the Pacific War were \n facilitated by the use of atomic weapons. China and Japan had been at war for four years prior to Pearl Harbor. \n Japan was ruled by Emperor Hirohito during the war. The American attempt to create an atomic weapon \n was known as the Manhattan Project. The Japanese attacked ships and planes during Pearl Harbor, but \n they notably left aircraft carriers unharmed. The code name for Germany's invasion of the Soviet Union was \n Operation Barbarossa. Blood, Toil, Tears, and Sweat is a quote from Winston Churchill's first speech as prime \n minister, which conveys determination in the face of difficulties.", bg = "#1F2833", font = ("Arial", 15))
    Overview_Information.config(fg = "#66FCF1")
    Overview_Information.pack(pady = 200)



    def Back_Page ():
        Information.destroy()
        Main_page()
    
    def Start_Quiz_page():
         Information.destroy()
         Open_Quiz()


    Back_button = tk.Button(Information, text = "Back", bg ="#1F2833", font=("Arial", 15), width = 7, height = 1, command=Back_Page)
    Back_button.config(fg="#66FCF1")
    Back_button.place(x=50,y=553)

    Start_Quiz_button = tk.Button(Information,text="Start Quiz", bg ="#1F2833", font=("Arial", 15), height = 1, width = 8, command=Start_Quiz_page)
    Start_Quiz_button.config(fg = "#66FCF1")
    Start_Quiz_button.place(x=800,y=550)

    Exit_button= tk.Button(Information, text="Exit", bg ='#1F2833',font=("Arial", 15), width = 7, height = 1, command=Information.destroy)
    Exit_button.config(fg = "#66FCF1")
    Exit_button.place(x=425, y=550)

    

    Information.mainloop()



# START THE QUIZ 
Answer_Entry = []
current_question_index = 0
score = 0



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
    global Answer_Entry, score
    question_label.config(text=Questions[current_question_index])
    for button in Answer_Entry:
        button.destroy()
        Answer_Entry = []
    for i, option in enumerate(Options[current_question_index]):
        Answer_Entry.append(tk.Button(quiz_frame, text=option, command=lambda selected_option=i: Check_Answer(selected_option), width = 45, height = 2, font = ("Arial", 15), bg = "#66FCF1"))
        Answer_Entry[i].pack(pady = 10)
    
def Final_Score():
    Score_Page = tk.Toplevel(quiz)
    Score_Page.title("Results")
    Score_Page.geometry("1000x700")
    Score_Page.configure(background="#1F2833")

    Score = tk.Label(Score_Page, text=f"Your score is {score}/{len(Questions)}", font=("Impact", 20), bg="#1F2833")
    Score.config(fg = "#66FCF1")
    Score.pack()

    percentage = (score / len(Questions)) * 100
    percentage_label = tk.Label(Score_Page, text=f"Percentage: {percentage:.2f}%", font=("Impact", 20), bg="#1F2833")
    percentage_label.config(fg = "#66FCF1")
    percentage_label.pack(pady=10)

    Exit_button = tk.Button(Score_Page, text="Exit", bg ='#1F2833',font=("Arial", 15), width = 7, height = 1, command=Score_Page.destroy)
    Exit_button.config(fg = "#66FCF1")
    Exit_button.place(x=425, y=550)

def Open_Quiz():
    global quiz, quiz_frame, question_label, Answer_Entry
    quiz = tk.Tk()
    quiz.title("WORLD WAR II")
    quiz.geometry("1200x700+100+100")
    quiz.configure(background="#1F2833")
    quiz.resizable(False, False)

    quiz_title = tk.Label(quiz, text="QUIZ", font=("Impact", 45), bg="#1F2833", padx=20, pady=10, borderwidth=2)
    quiz_title.config(fg="#66FCF1")
    quiz_title.pack()

    quiz_frame = tk.Frame(quiz, bg="#1F2833")
    quiz_frame.pack(pady=20)

    question_label = tk.Label(quiz_frame, text=Questions[current_question_index], font=("Arial", 15), bg = "#1F2833")
    question_label.config(fg="#66FCF1")
    question_label.pack(pady = 20, padx = (0))

    Exit_button = tk.Button(quiz, text="Exit", bg ='#1F2833',font=("Arial", 15), width = 7, height = 1, command=quiz.destroy)
    Exit_button.config(fg = "#66FCF1")
    Exit_button.place(x=425, y=550)

    Get_Question()

    quiz.mainloop()

    Quiz_Title = tk.Label(quiz, text="Quiz", font=("Impact", 45), bg="#1F2833", padx=20, pady=10, border_width=2)
    Quiz_Title.pack()
    
    

    question_label = tk.Label(quiz, text=Questions[current_question_index], font=("Arial", 15))
    question_label.pack()





    Get_Question()

Main_page()     
