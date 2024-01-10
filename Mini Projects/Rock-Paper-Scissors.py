import random
import tkinter

window = tkinter.Tk()
window.geometry("1000x500")
window.title("Rock - Paper - Scissors Game")

user_score = 0
computer_score = 0
userChoice = ""
computerChoice = ""


# 0 = rock, 1 = paper, 2 = scissors 
def randomizeComputerChoice():
    global computerChoice
    computerChoice = random.choice([0,1,2])

def changeUserChoice(choice):
    global userChoice
    userChoice = choice

def result():
    global userChoice
    global computerChoice
    global user_score
    global computer_score

    if(userChoice == computerChoice):
        print("Tie!!!")
    elif((userChoice - computerChoice)%3 == 1):
        print("User wins!!!")
        user_score = user_score + 1
    else:
        print("Computer Wins!!!")
        computer_score = computer_score + 1

    text_area = tkinter.Text(master=window, height=100, width=50, bg="#FFFF99")
    text_area.grid(column=0, row=4)

    rps = ["rock", "paper", "scissors"]
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=rps[userChoice],cc=rps[computerChoice],u=user_score,c=computer_score)    
    text_area.insert(tkinter.END,answer)

def rockButton():
    global userChoice
    userChoice = 0 #rock
    randomizeComputerChoice()
    result()

def paperButton():
    global userChoice
    userChoice = 1 #paper
    randomizeComputerChoice()
    result()

def scissorsButton():
    global userChoice
    userChoice = 2 #scissors
    randomizeComputerChoice()
    result()

#create the buttons for the user:
button1 = tkinter.Button(text="Rock", bg="skyblue", command=rockButton)
button1.grid(column=1,row=0)

button2 = tkinter.Button(text="Paper", bg="skyblue", command=paperButton)
button2.grid(column=2,row=0)

button3 = tkinter.Button(text="Scissors", bg="skyblue", command=scissorsButton)
button3.grid(column=3,row=0)

window.mainloop()