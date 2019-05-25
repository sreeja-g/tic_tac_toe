from tkinter import *
import GAME

row = 3
coloumn = 3
def call(root):
    game_instance=Game_gui(root)
    Game(game_instance)
    root.resizable(width=False, height=False)
    root.mainloop()


#____________________________________________________START_GAME__________________________________________________________


def win(gui):
    winning_values=[[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8]]
    for i in winning_values:
        count=[0,0]
        for j in i:
            if gui.button[j].cget('text') == 'X':
                count[0]+=1
            elif gui.button[j].cget('text') == 'O':
                count[1] += 1
        if count[0]==3 or count[1]==3:
            for k in i:
                gui.button[k].config(disabledforeground='red')
            return True
    return False

def tie(gui):
    count=0
    for i in gui.button:
        if i['state'] == 'disabled':
            count+=1
    if count == 9:
        return True
    else:
        return False

class Game_gui():

    def __init__(self,root):
        #___________________________________________________player_name__________________________________________________________
        self.player='X'
        self.labelfont = ('times', 20, 'bold')
        frame=Frame(root,bg='pink')
        frame.pack(fill=X)

        frame1=Frame(frame,bg='pink')
        frame1.pack()

        button1 = Button(frame1, width=14, height=3, bg='lightblue', text='BACK',
                         command=GAME.combine_funcs(frame.destroy,frame1.destroy, lambda: GAME.call(root)))
        button1.pack(side=LEFT, padx=4)

        self.label = Label(frame1, text=self.print_player())
        self.label.config(bg='pink', fg='white', font=self.labelfont, height=3, width=20)
        self.label.pack(side=LEFT)

        button2 = Button(frame1, width=14, height=3, bg='lightblue', text='RESTART',
                         command=GAME.combine_funcs(frame.destroy,frame1.destroy, lambda: call(root)))
        button2.pack(side=LEFT, padx=4)

        #___________________________________________________game_space__________________________________________________________

        self.button_font= ('times', 12, 'bold')
        self.frames=[]
        for i in range(coloumn):
            self.frames.append(Frame(frame,bg='white'))
            self.frames[i].pack(fill=X)

        self.button=['','','','','','','','','']
        self.button_text =[]
        for i in range(row):
            for j in range(coloumn):
                self.button_text.append(' ')
                self.button[3*i+j]=(Button(self.frames[i],font=self.button_font,text=self.button_text[3*i+j],bg='lightblue',width=20,height=5))

        for i in range(row*coloumn):
            self.button[i].grid(row=i//3,column=i%3)

    def print_player(self):
        return 'player ' + self.player + "'s turn"



class Game():

    def __init__(self,gui):
        gui.button[0].config(command=lambda: self.called(gui.button[0],gui))
        gui.button[1].config(command=lambda: self.called(gui.button[1],gui))
        gui.button[2].config(command=lambda: self.called(gui.button[2],gui))
        gui.button[3].config(command=lambda: self.called(gui.button[3],gui))
        gui.button[4].config(command=lambda: self.called(gui.button[4],gui))
        gui.button[5].config(command=lambda: self.called(gui.button[5],gui))
        gui.button[6].config(command=lambda: self.called(gui.button[6],gui))
        gui.button[7].config(command=lambda: self.called(gui.button[7],gui))
        gui.button[8].config(command=lambda: self.called(gui.button[8],gui))

    def called(self, button,gui):
        button.config(text=gui.player,state=DISABLED)
        self.game_check(gui)

    def game_check(self,gui):


        if win(gui) == True:
            self.game_finished(gui)
            return

        if tie(gui) == True:
            gui.label.config(text="It's a tie")
            return


        if gui.player == 'X':
            gui.player = 'O'
        else:
            gui.player = 'X'

        gui.label.config(text=gui.print_player())

    def game_finished(self,gui):
        gui.label.config(text=gui.player + ' won')
        for i in gui.button:
            i.config(state=DISABLED)



