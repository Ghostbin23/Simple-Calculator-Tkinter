from tkinter import *

# add error catching/describing 
# add more complicated mathematical symbols (thinking of how eval() works!)
# using result 

express = ""

def press(key):
    global express # ensures we're using a global "express" variable
    express += str(key)
    display.set(express) # changes display "stringvar" to be new expression

def equal():
    global express
    try:
        if express == "9+10":
            result = "21 lol"
        else:
            result = str(eval(express)) # eval() evaluates an input string as though it is a python expression
        display.set(result) # displays result of this evaluation
        express = result
    except:
        display.set("ERROR!")
        express = ""

def clear():
    global express
    express = ""
    display.set("")

root = Tk()
root.configure(bg = "light blue")
root.title("Basic Calculator")
root.geometry("270x150")

display = StringVar() # tkinter stringvar is somewhere where we can hold text inputs/receive text inputs
entry = Entry(root, textvariable=display) # tkinter entry holds this entry and assigns it to show stringvar "display", it's the graphical depiction
entry.grid(columnspan=4,ipadx = 70) # spans across 4 columns with padding in the x axis

# Number buttons
btn1 = Button(root, text='1', fg='black', bg='light green', command=lambda: press(1), height=1, width=7) # lambda becuz we need to passa arguments
btn1.grid(row=2, column=0)
btn2 = Button(root, text='2', fg='black', bg='light green', command=lambda: press(2), height=1, width=7)
btn2.grid(row=2, column=1)
btn3 = Button(root, text='3', fg='black', bg='light green', command=lambda: press(3), height=1, width=7)
btn3.grid(row=2, column=2)
btn4 = Button(root, text='4', fg='black', bg='light green', command=lambda: press(4), height=1, width=7)
btn4.grid(row=3, column=0)
btn5 = Button(root, text='5', fg='black', bg='light green', command=lambda: press(5), height=1, width=7)
btn5.grid(row=3, column=1)
btn6 = Button(root, text='6', fg='black', bg='light green', command=lambda: press(6), height=1, width=7)
btn6.grid(row=3, column=2)
btn7 = Button(root, text='7', fg='black', bg='light green', command=lambda: press(7), height=1, width=7)
btn7.grid(row=4, column=0)
btn8 = Button(root, text='8', fg='black', bg='light green', command=lambda: press(8), height=1, width=7)
btn8.grid(row=4, column=1)
btn9 = Button(root, text='9', fg='black', bg='light green', command=lambda: press(9), height=1, width=7)
btn9.grid(row=4, column=2)
btn0 = Button(root, text='0', fg='black', bg='light green', command=lambda: press(0), height=1, width=7)
btn0.grid(row=5, column=1)

# Operator buttons
plus = Button(root, text='+', fg='black', bg='light green', command=lambda: press('+'), height=1, width=7)
plus.grid(row=2, column=3)
minus = Button(root, text='-', fg='black', bg='light green', command=lambda: press('-'), height=1, width=7)
minus.grid(row=3, column=3)
mult = Button(root, text='*', fg='black', bg='light green', command=lambda: press('*'), height=1, width=7)
mult.grid(row=4, column=3)
div = Button(root, text='/', fg='black', bg='light green', command=lambda: press('/'), height=1, width=7)
div.grid(row=5, column=3)
indice = Button(root, text='^', fg='black', bg='light green', command=lambda: press('**'), height=1, width=7)
indice.grid(row=6, column=3)
obrack = Button(root, text='(', fg='black', bg='light green', command=lambda: press('('), height=1, width=7)
obrack.grid(row=5, column=0)
cbrack = Button(root, text=')', fg='black', bg='light green', command=lambda: press(')'), height=1, width=7)
cbrack.grid(row=5, column=2)

# Other buttons
eq = Button(root, text='=', fg='black', bg='red', command=equal, height=1, width=7)
eq.grid(row=6, column=2)
clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
clr.grid(row=6, column=1)
dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
dot.grid(row=6, column=0)

root.mainloop()

