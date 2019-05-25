from tkinter import *
import single_player_XOXO,multi_player_XOXO

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class home():

    def __init__(self,root):
        frame=Frame(root,bg='lightblue')
        frame.pack()

        button1 = Button(frame,bg='pink',width=20,height=5,text='SINGLE PLAYER',command=combine_funcs(frame.destroy,lambda :single_player_XOXO.call(root)))
        button1.grid(row=0,column=0,padx=75,pady=75)
        button2 = Button(frame,bg='pink',width=20,height=5,text='MULTI PLAYER',command=combine_funcs(frame.destroy,lambda :multi_player_XOXO.call(root)))
        button2.grid(row=0,column=1,padx=75,pady=75)
        button3 = Button(frame,bg='pink',width=20,height=3,text='QUIT')
        button3.config(command=root.destroy)
        button3.grid(row=2,columnspan=2,pady=75)

def call(root):
    home(root)
    root.mainloop()

if __name__=="__main__":
    root=Tk()
    home(root)
    root.mainloop()


