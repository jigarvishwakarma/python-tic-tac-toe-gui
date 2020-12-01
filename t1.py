from tkinter import *
from tkinter import messagebox
import pygame
from pygame import mixer
global fg1,bg2,bg1
bg1="#615955"
fg1= "white"
bg2= "#e67740"

try :
    mixer.init()
    mixer.music.load("cartoon.mp3")
except:
    print("Music file is not found")

def tictactoe():
    root=Tk()
    root.title("The Real Tic Tac Toe")
    root.configure(background=bg1)
    root.bind('<Key>', lambda a : key_press(a))
    #================================Variables==============================
    player1=name1.get()
    player2=name2.get()
    global chance,turns,value1,value2,value3,value4,value5,value6,value7,value8,value9,chance
    turns=1
    value1="01"
    value2="02"
    value3="03"
    value4="04"
    value5="05"
    value6="06"
    value7="07"
    value8="08"
    value9="09"

    #================================Functions==============================
    def checkPossibilities():
        global turns,record
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,chance
        if turns<9:
            if value1==value2 and value2==value3 :
                record=turns 
                result.set(value1)
                if value1=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value1+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value1+") is winner")
            elif value4==value5 and value5==value6:
                record=turns
                result.set(value4)
                if value4=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value4+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value4+") is winner")
            elif value7==value8 and value8==value9:
                record=turns
                result.set(value7)
                if value7=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value7+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value7+") is winner")
            elif value1==value4 and value4==value7:
                record=turns
                result.set(value7)
                if value7=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value7+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value7+") is winner")
            elif value8==value5 and value5==value2:
                record=turns
                result.set(value5)
                if value5=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value5+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value5+") is winner")
            elif value9==value6 and value6==value3:
                result.set(value9)
                record=turns
                if value9=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value9+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value9+") is winner")
            elif value1==value5 and value5==value9:
                result.set(value1)
                record=turns
                if value1=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value1+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value1+") is winner")
            elif value7==value5 and value5==value3:
                record=turns
                result.set(value7)
                if value7=="X":
                    messagebox.showinfo("WINNER IS..", "congratulations " +player1+" ("+value7+") is winner")
                else:
                    messagebox.showinfo("WINNER IS..", "congratulations " +player2+" ("+value7+") is winner")
            else:
                record=turns

            v=defineChance()
            if v=="X":
                showchance=str(player2+"'s turn")
                show=Label(root,text=showchance,font=('arial', 19,"bold"),bg=bg1,fg=fg1,width=20).grid(row=35,column=10,columnspan=21)
            else:
                showchance=str(player1+"'s turn")
                show=Label(root,text=showchance,font=('arial', 19,"bold"),bg=bg1,fg=fg1,width=20).grid(row=35,column=10,columnspan=21)
        else:
            messagebox.showinfo("IT'S A DRAW MATCH.. ")
        turns=turns+1
    show=Label(root,text=player1+"'s turn",font=('arial', 19,"bold"),bg=bg1,fg=fg1,width=20).grid(row=35,column=10,columnspan=21) 
            
    def defineChance():
        if(turns%2==0):
            chance="O"
            return chance 
        else:
            chance="X"
            return chance
    
    defineChance()
    def b1():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value1=defineChance()
        btton1=Button(root,text=value1,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=20,column=11,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass
        

    def b2():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value2=defineChance()
        btton2=Button(root,text=value2,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=20,column=15,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def b3():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value3=defineChance()
        btton3=Button(root,text=value3,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=20,column=19,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def b4():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value4=defineChance()
        btton4=Button(root,text=value4,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=24,column=11,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def b5():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value5=defineChance()
        btton5=Button(root,text=value5,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=24,column=15,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def b6():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value6=defineChance()
        btton6=Button(root,text=value6,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=24,column=19,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def b7():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value7=defineChance()
        btton7=Button(root,text=value7,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=28,column=11,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def b8():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value8=defineChance()
        btton8=Button(root,text=value8,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=28,column=15,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass
        
    def b9():
        global value1,value2,value3,value4,value5,value6,value7,value8,value9,turns
        value9=defineChance()
        btton9=Button(root,text=value9,height=7,width=15,font=('arial', 9,"bold"),bg=bg2,fg=fg1).grid(row=28,column=19,columnspan=2)
        checkPossibilities()
        try:
            mixer.music.play()
        except:
            pass

    def key_press(event): 
        key = event.char
        if key=="1":
            b1()
        elif key=="2":
            b2()
        elif key=="3":
            b3()
        elif key=="4":
            b4()
        elif key=="5":
            b5()
        elif key=="6":
            b6()
        elif key=="7":
            b7()
        elif key=="8":
            b8()
        else:
            b9()
    #================================GUI Part==============================
        
    Title = Label(root,text='The Real Tic Tac Toe',font=('arial', 22,"bold"),bg=bg1,fg=fg1)
    Title.grid(row=10 ,column=11,rowspan=4 ,columnspan=12)
    name=str("{}  VS  {}").format(player1,player2)
    info=Label(root,text=name,font=('arial', 11,"italic"),bg=bg1,fg=fg1).grid(row=16 ,column=11,rowspan=4 ,columnspan=12)
    result = StringVar()
    result.set("")
    res=Label(root,textvariable=result,bg=bg1,fg=fg1).grid(row=50,column=15,columnspan=2)

    #================================Buttons==============================
    
    btton1=Button(root,text="",command=b1,height=7,width=15,bg=bg2).grid(row=20,column=11,columnspan=2)
    btton2=Button(root,text="",command=b2,height=7,width=15,bg=bg2).grid(row=20,column=15,columnspan=2)
    btton3=Button(root,text="",command=b3,height=7,width=15,bg=bg2).grid(row=20,column=19,columnspan=2)
    btton4=Button(root,text="",command=b4,height=7,width=15,bg=bg2).grid(row=24,column=11,columnspan=2)
    btton5=Button(root,text="",command=b5,height=7,width=15,bg=bg2).grid(row=24,column=15,columnspan=2)
    btton6=Button(root,text="",command=b6,height=7,width=15,bg=bg2).grid(row=24,column=19,columnspan=2)
    btton7=Button(root,text="",command=b7,height=7,width=15,bg=bg2).grid(row=28,column=11,columnspan=2)
    btton8=Button(root,text="",command=b8,height=7,width=15,bg=bg2).grid(row=28,column=15,columnspan=2)
    btton9=Button(root,text="",command=b9,height=7,width=15,bg=bg2).grid(row=28,column=19,columnspan=2)
    root.mainloop()

    
root1=Tk()
root1.title("Please Enter name")
root1.minsize(330,300)
root1.configure(background=bg1)

Title = Label(root1,text='The Real Tic Tac Toe',font=('arial', 18,"bold"),fg=bg2,bg=bg1)
Title.grid(row=10 ,column=10,rowspan=4 ,columnspan=120)
player1=Label(root1,text="Enter player 1 name: ",font=('arial', 10,"bold"),fg=fg1,bg=bg1).grid(row=20,column=10,columnspan=3)
player2=Label(root1,text="Enter player 2 name: ",font=('arial', 10,"bold"),fg=fg1,bg=bg1).grid(row=35,column=10,columnspan=3)
name1=Entry(root1,width=30)
name1.grid(row=20,column=30,columnspan=3)
name2=Entry(root1,width=30)
name2.grid(row=35,column=30,columnspan=3)
start=Button(root1,text="START",command=tictactoe,width=30,font=('arial', 11,"bold"),bg=bg2,fg=fg1).grid(row=40,column=10,columnspan=50)
Exit=Button(root1,text="EXIT",command=exit,width=30,font=('arial', 11,"bold"),bg=fg1,fg=bg2).grid(row=60,column=10,columnspan=50)
btn10=StringVar()
btton19=Button(root1,text="Pick color",bg=bg1,width=18,fg=fg1,font=('arial', 9,"bold"),relief=FLAT).grid(row=65,column=10,columnspan=20)
root1.mainloop()
