from tkinter import *
import random


root = Tk()
root.resizable(False,False)
root.title('Wordle Python')
root.call("source", "azure.tcl")


my_file = open("slova.txt", "r",encoding="utf8")
wordlist = my_file.read().split('\n')
my_file.close()

TESTWORD = wordlist[random.randint(0,len(wordlist))]


position = 0
guessword = ""

def change_theme():
    if root.call("ttk::style", "theme", "use") == "azure-dark":
        root.call("set_theme", "light")
    else:
        root.call("set_theme", "dark")

darklight_button = Button(text="Light/Dark Mode", width=35, command=change_theme)
darklight_button.pack(padx=1)

def generate_word():
    return wordlist[random.randint(0,len(wordlist))]

def newgame():
    global position
    global TESTWORD
    TESTWORD = generate_word()
    word_guess.delete(0, len(word_guess.get()))
    position = 0
    status['text'] = "Wordle Python"
    reset_btn.config(bg='#f0f0f0')
    for i in range(6):
        for j in range(5):
            tiles[i][j]['text'] = ""
            tiles[i][j].config(bg="#f0f0f0")

def show_ans():
    status['text'] = f"slovo je {TESTWORD}"

def send_word():
    guess = word_guess.get()
    if len(guess.strip().lower()) != 5 : word_guess.delete(0,len(guess))
    else:
        word_guess.delete(0, len(guess))
        guess = guess.strip().lower()
        print(guess)
        i = 0
        global position
        global guessword
        guessword = guess

        for c in guess:
            tiles[position][i]['text'] = c
            i += 1
        check_word()
        position+=1
        print(position)
        if position == 6:
            status['text'] = f"Prohra slovo bylo: {TESTWORD}"
            reset_btn.config(bg='#ed766d')

def check_word():
    global guessword
    global position

    tmp = list(guessword)
    tmp2 = list(TESTWORD)

    for i in range(len(tmp2)):
        if guessword[i] not in tmp2:
                tiles[position][i].config(bg="#858585")

    for i in range(len(guessword)):
        if guessword[i] == tmp2[i]:
            tiles[position][i].config(bg="#66e362")
            tmp2[tmp2.index(guessword[i])] = '#'
            print(tmp2)

    for i in range(len(tmp2)):
        if guessword[i] in tmp2:
                tiles[position][i].config(bg="#e3d462")
                tmp2[tmp2.index(guessword[i])] = '#'

    for i in tiles[position]:
        if i['bg'] == "SystemButtonFace":
            i.config(bg="#858585")

    if guessword == TESTWORD:
        status['text'] = 'Jsi nejlepší 🤬😎💯🥰♥'
        reset_btn.config(bg='#ed766d')

tiles = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

heading = Label(text="worlde 👌💪", font=("Helvetica",30))
heading.pack(side="top")


btnframe = Frame(root)
btnframe.pack()

reset_btn = Button(btnframe,text="Reset", font=("Helvetica",15),command=newgame)
reset_btn.pack(side=LEFT,padx=2)

show_ans_btn = Button(btnframe,text="Odpověď",command=show_ans,font=("Helvetica",15))
show_ans_btn.pack(side=RIGHT)

status = Label(text="PyWordle", font=("Helvetica",15))
status.pack(pady=2)

tileframe = Frame(root) # letter tiles
tileframe.pack(padx=15)

for row in range(6):
    for col in range(5):
        tiles[row][col] = Button(tileframe,text="",font=("Helvetica",15),width=5,height=2)
        tiles[row][col].grid(row=row,column=col)

enterframe = Frame(root)
enterframe.pack(pady=10)

word_guess = Entry(enterframe,width=10,font=("Helvetica",15),borderwidth=5)
word_guess.pack(side=LEFT)
enter_btn = Button(enterframe,text="Zadat",command=send_word,font=("Helvetica",15))
enter_btn.pack(side=RIGHT)




root.mainloop()