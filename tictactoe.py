from tkinter import *
import tkinter.messagebox as msg
#window

screen = Tk()
screen.title("Tic-Tac-Toe")

#label

Label(screen,text = "player1 = X",font = "Times 25").grid(row = 0,column = 1)
Label(screen,text = "player2 = O",font = "Times 25").grid(row = 0,column = 2)

digits= [1,2,3,4,5,6,7,8,9]
#p1 X and p2 O
mark =''

#count to keep no. of clicks
count = 0

#panel is a container
panels = ["panel"] * 10

#function
def win(panels,sign):
    return((panels[1]==panels[2]==panels[3]==sign)
          or (panels[1]==panels[5]==panels[9]==sign)
          or (panels[2]==panels[5]==panels[8]==sign)
          or (panels[3]==panels[6]==panels[9]==sign)
          or (panels[1]==panels[5]==panels[7]==sign)
          or (panels[1]==panels[4]==panels[7]==sign)
          or (panels[4]==panels[5]==panels[6]==sign)
          or (panels[7]==panels[8]==panels[9]==sign))


def checker(digit):
    global count,mark,digits

    #check which button id clicked
    if digit ==1 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button1.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    
    #button 2
    if digit ==2 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button2.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button3
    if digit ==3 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button3.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button 4
    if digit ==4 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button4.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button 5
    if digit ==5 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button5.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button 6
    if digit ==6 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button6.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button7
    if digit ==7 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button7.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button 8
    if digit ==8 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button8.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    #button9
    if digit ==9 and digit in digits:
        digits.remove(digit)


        if count % 2 == 0:
            mark = 'O'
            panels[digit] = mark
        elif count % 2 != 0:
            mark = 'X'
            panels[digit] = mark
        
        button9.config(text = mark)
        count = count+1
        sign = mark

        if win(panels,sign) and sign == 'X':
            msg.showinfo("Result","player1 wins!")
            screen.destroy()
        elif win(panels,sign) and sign == 'O':
            msg.showinfo("Result","player2 wins!")
            screen.destroy()
    if (count>8 and win(panels,'X')==False and win(panels,'O')==False):
        msg.showinfo("result","It is a tie")
        screen.destroy()

#buttons
button1 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(1))
button1.grid(row= 1,column = 1)
button2 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(2))
button2.grid(row= 1,column = 2)
button3 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(3))
button3.grid(row= 1,column = 3)
button4 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(4))
button4.grid(row= 2,column = 1)
button5 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(5))
button5.grid(row= 2,column = 2)
button6 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(6))
button6.grid(row= 2,column = 3)
button7 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(7))
button7.grid(row= 3,column = 1)
button8 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(8))
button8.grid(row= 3,column = 2)
button9 = Button(screen,width=15,height=7,font = ("Arial 20 bold"),command=lambda:checker(9))
button9.grid(row= 3,column = 3)

screen.mainloop()
