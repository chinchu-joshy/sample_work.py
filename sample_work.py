from tkinter import *

operator = ""


def enter(num):
    global operator
    operator = operator + str(num)
    equation.set(operator)


def clearClick():
    global operator
    operator = ""
    equation.set("")


def equelButton():
    global operator
    answer = str(eval(operator))
    equation.set(answer)


window = Tk()
window.title("calculator")
window.configure(background="light green")
equation = StringVar()
textDisplay = Entry(window, textvariable=equation, font=('areal', 20, 'bold'), insertwidth=7, bg="green")
textDisplay.grid(columnspan=6)
equation.set('hello')
btn1 = Button(window, text='7', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(7))
btn2 = Button(window, text='8 ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(8))
btn3 = Button(window, text=' 9', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(9))

btn4 = Button(window, text='+ ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter('+'))
btn5 = Button(window, text='4', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(4))
btn6 = Button(window, text='5 ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(5))
btn7 = Button(window, text='6', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(6))
btn8 = Button(window, text='- ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter('-'))
btn9 = Button(window, text='1', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
              command=lambda: enter(1))
btn10 = Button(window, text='2', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=lambda: enter(2))
btn11 = Button(window, text='3', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=lambda: enter(3))
btn12 = Button(window, text='* ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=lambda: enter('*'))
btn13 = Button(window, text='. ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=lambda: enter("."))
btn14 = Button(window, text='0', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=lambda: enter(0))
btn15 = Button(window, text='= ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=equelButton)
btn16 = Button(window, text='/ ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=lambda: enter('/'))
btn17 = Button(window, text='clear ', bd='3', font=('areal', 20, 'bold'), height=3, width=7, bg="blue",
               command=clearClick)
btn1.grid(row=1, column=1, )
btn2.grid(row=1, column=2, )
btn3.grid(row=1, column=3, )
btn4.grid(row=1, column=4, )
btn5.grid(row=2, column=1, )
btn6.grid(row=2, column=2, )
btn7.grid(row=2, column=3, )
btn8.grid(row=2, column=4, )
btn9.grid(row=3, column=1, )
btn10.grid(row=3, column=2, )
btn11.grid(row=3, column=3, )
btn12.grid(row=3, column=4, )
btn13.grid(row=4, column=1, )
btn14.grid(row=4, column=2, )
btn15.grid(row=4, column=3, )
btn16.grid(row=4, column=4, )
btn17.grid(row=5, column=2)
window.mainloop()
