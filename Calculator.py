from tkinter import *
express = ""
def press(key):
    global express
    express += str(key)
    display.set(express)
def equal():
    global express
    try:
        if express == "9+10":
            result = "21 lol"
        else:
            result = str(eval(express))
        display.set(result)
        express = result
    except:
        display.set("ERROR!")
        express = ""
def clear():
    global express
    express = ""
    display.set("")
root = Tk()
root.configure(bg="light blue")
root.title("Basic Calculator")
root.geometry("270x150")
display = StringVar()
entry = Entry(root, textvariable=display)
entry.grid(columnspan=4, ipadx=70)
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
    ('0', 5, 1), ('.', 6, 0)
]
for (text, row, col) in buttons:
    Button(root, text=text, fg='black', bg='light green',
           command=lambda x=text: press(x), height=1, width=7)\
        .grid(row=row, column=col)
ops = [
    ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3),
    ('^', 6, 3), ('(', 5, 0), (')', 5, 2)
]
for (text, row, col) in ops:
    cmd = lambda x=text: press('**' if x == '^' else x)
    Button(root, text=text, fg='black', bg='light green',
           command=cmd, height=1, width=7)\
        .grid(row=row, column=col)
specials = [
    ('=', 6, 2, equal), ('Clear', 6, 1, clear)
]
for (text, row, col, func) in specials:
    Button(root, text=text, fg='black', bg='red',
           command=func, height=1, width=7)\
        .grid(row=row, column=col)
root.mainloop()
