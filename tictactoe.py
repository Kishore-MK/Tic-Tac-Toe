from tkinter import *
import random

def next_t(row,column):

    global player

    if buttons[row][column]['text']=="" and win() is False:

        if player == players[0]:

            buttons[row][column]['text']=player

            if win() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))

            elif win() is True:
                label.config(text=players[0]+" wins")

            elif win() == "tie":
                label.config(text="Tie!!")
        else:
            buttons[row][column]['text']=player

            if win() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))
            elif win() is True:
                label.config(text=(players[1]+" wins"))
            elif win() == "tie":
                label.config(text="Tie!!")



def win():

    for row in range(5):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text']== buttons[row][3]['text']== buttons[row][4]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            buttons[row][3].config(bg="green")
            buttons[row][4].config(bg="green")
            return True
        
    for col in range(5):
        if buttons[0][col]['text'] == buttons[1][col]['text']==buttons[2][col]['text']==buttons[3][col]['text']==buttons[4][col]['text']!="":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            buttons[3][col].config(bg="green")
            buttons[4][col].config(bg="green")
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']==buttons[3][3]['text']==buttons[4][4]['text']!="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        buttons[3][3].config(bg="green")
        buttons[4][4].config(bg="green")

        return True
    elif buttons[0][4]['text']==buttons[1][3]['text']==buttons[3][3]['text']==buttons[3][1]['text']==buttons[4][0]['text']!="":
        buttons[0][4].config(bg="green")
        buttons[1][3].config(bg="green")
        buttons[3][3].config(bg="green")
        buttons[3][1].config(bg="green")
        buttons[4][0].config(bg="green")
        return True
    elif empty() is False:
        for row in range(5):
            for column in range(5):
                buttons[row][column].config(bg="yellow")
        return "tie"
    else:
        return False

def empty():
    spaces = 25

    for row in range(5):
        for column in range(5):
            if buttons[row][column]['text']!="":
                spaces-=1
    if spaces == 0:            
        return False
    else:
        return True

def new():
    global player

    player = random.choice(players)

    label.config(text=player+"'s turn")

    for row in range(5):
        for column in range(5):
            buttons[row][column].config(text="",bg="#F0F0F0")



root = Tk()
root.title("Tic Tac Toe")
players=["X","O"]
player=random.choice(players)
buttons=[[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],]
label = Label(text=player+"'s turn",font=('sans serif',40))
label.pack(side="top")

reset = Button(text="restart",font=('sans serif',15),command=new)
reset.pack(side="top")

frame = Frame(root)
frame.pack()

for row in range(5):
    for column in range(5):
        buttons[row][column] = Button(frame,text="",font=('sans serif',40),
        height=1
        ,width=3,command=lambda row=row, column=column: next_t(row,column))
        buttons[row][column].grid(row=row,column=column)
root.mainloop()