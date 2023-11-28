import tkinter as tk
from tkinter import ttk
import random as rn
import pickle as pk

vocabular=pk.load(open("spanish.txt","rb"))
wordlist=vocabular.keys()
new=rn.sample(wordlist,k=1)
def nextflashcard(): 
    word=vocab.cget("text")
    new=rn.sample(wordlist,k=1)
    vocab.config(text=new[0],background='#fff')
    entry.delete(0,"end")
    
def show():
    word=vocab.cget("text")
    answer=vocabular.get(word)
    vocab.config(text=answer,background='#0ff')
    
def test():
    word=vocab.cget("text")
    test=entry.get()
    entry.delete(0,"end")
    answer=vocabular.get(word)
    if test==answer:
        vocab.config(background='#0f0')
    else:
        vocab.config(background='#f00')
        
# root window
root = tk.Tk()
root.geometry('300x300')
root.title('FlashCards')
root.configure(background='#fff')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

#widgets
vocab=ttk.Label(root,text=new[0],font=('Ariel',25),background='#fff')
entry=ttk.Entry(root)
test=ttk.Button(root,text="test",command=test)
show=ttk.Button(root,text="show",command=show)
nextt=ttk.Button(root,text="next",command=nextflashcard)

vocab.pack(expand='True')
entry.pack(expand='True')
test.pack(expand='True')
show.pack(expand='True')
nextt.pack(expand='True')

root.mainloop()