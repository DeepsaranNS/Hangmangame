import sys
import string
dashes=None
#print('\n\033[1m Player 1:Questioning person')
#print('\033[1m Player 2:Answering person')
#hid_word=input('\n\033[1m Player 1,please enter your hidden word :')
def get_hidden():
    global hidden,hid_word,dashes_var,dashes
    hid_word=hidden.get().lower()
    dashes=['_']*len(hid_word)
    dashes_var['text']=''.join(x+''for x in dashes)
    dashes_var.pack()
    hidden.destroy()

hid_word=''
chances=7
cur_count=1

def display_dashes():
    global dashes
    for x in dashes:
        print(x,end=' ')

def get_moves():
    global hid_word,dashes,chances,ltr_inp,chances_var,dashes_var,present_var,cur_count,hangman_img,img,hidden,btn2

    letter=ltr_inp.get().lower()
    if len(letter)>1:
       present_var['text']='enter only one letter'
       present_var.pack()
       # print('\n\o33[1m enter only one letter')
    elif letter not in string.ascii_letters:
        present_var['text'] = 'Please!!! enter a letter'
        present_var.pack()

    else:
        ans=''
        if letter in hid_word:
            ans='The letter guessed is present in the word'
            for x in range(len(hid_word)):
                if letter==hid_word[x]:
                   dashes[x]=letter

        else:
          ans=' Sorry!! the letter is not in the hidden word'
          img=PhotoImage(file=f'Hangman_pics\hangman_step{cur_count}.png')
          hangman_img['image']=img
          hangman_img.pack()
          cur_count+=1




        chances-=1
        present_var['text']=ans
        present_var.pack()
        dashes_var['text']=''.join(x+' 'for x in dashes)
        dashes_var.pack()
        chances_var['text']="chances left :"+str(chances)
        chances_var.pack()
        print('\n chances left',chances)
        #ltr_inp.insert(0, "")
        ltr_inp.delete(0, END)
        check_win()

def check_win():
    global hid_word,dashes,chances
    if chances==0:
        #print('\n\033[1m you lost the game,the hidden word is:',hid_word)
        present_var['text']=' You lost the game,the hidden word is:'+hid_word
        present_var.pack()
    else:
        flg=0
        for x in dashes:
            if x=='_':
                flg=1
        if flg==0:
            #print('\n\n\n\033[1m You won the game')
            present_var['text']='YOU WON THE GAME'
            present_var.pack()



###########################################################################################

from tkinter import Tk
from tkinter import *
from tkinter import font
root=Tk()
ff=font.Font(size=30)
def print_letter():
    global ltr_inp
    print(ltr_inp.get())
heading=Label(root,text='HANGMAN GAME ')
heading.pack()
heading['font']=ff
heading1=Label(root,text='Player1: Type the hidden word,within 6 letters ')
heading1.pack()
heading1['font']=ff
heading2=Label(root,text='Player2:Guess the hidden word ')
heading2.pack()
heading2['font']=ff
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
hidden=Entry(frame1)
hidden.pack()
hidden['font']=ff
btn2=Button(frame1,text='hide',command=get_hidden)
btn2.pack()
btn2['font']=ff
img=PhotoImage(file='C:\\Users\\deeps\\PycharmProjects\\Hangman_game\\Hangman_pics\\hangman_step1.png')
hangman_img=Label(frame1,image=img)
hangman_img.pack()
dashes_var=Label(frame1,text='_ '*len(hid_word))
dashes_var.pack()
dashes_var['font']=ff
chances_var=Label(frame1,text='chances remaining :7 ')
chances_var.pack()
chances_var['font']=ff
present_var=Label(frame1,text='present or not')
present_var.pack()
present_var['font']=ff
ltr_inp=Entry(frame2)
ltr_inp.grid(row=0,column=0)
ltr_inp['font']=ff
btn=Button(frame2,text='Guess the word',command=get_moves)
btn.grid(row=0,column=1)
btn['font']=ff


mainloop()

