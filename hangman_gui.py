from tkinter import Tk
from tkinter import *
from tkinter import font
root=Tk()

def print_letter():
    global letter_input
    print(letter_input.get())

ff=font.Font(size='25')
heading=Label(root,text="Hangman Game")
heading.pack()
heading['font']=ff
f1=Frame(root)
f2=Frame(root)
f1.pack()
f2.pack()
img=PhotoImage(file='C:\\Users\\Balarubinan\\PycharmProjects\\Hangman_game\\hangman_pics\\hangman_step5.png')
hang_man_img=Label(f1,image=img)
hang_man_img.pack()
hang_man_img['font']=ff
dash_label=Label(f1,text='_ '*7)
dash_label.pack()
dash_label['font']=ff
chance_label=Label(f1,text='present')
chance_label.pack()
chance_label['font']=ff

present_label=Label(f1,text='chances left is : 10')
present_label.pack()
present_label['font']=ff

letter_input=Entry(f2)
letter_input.grid(row=0,column=0)
letter_input['font']=ff
btn=Button(f2,text='Guess',command=print_letter)
btn.grid(row=0,column=1)
btn['font']=ff
root.mainloop()