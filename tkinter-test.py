from tkinter import *
import os

def rcpath(rel_path):
    return os.path.join(os.getcwd(), rel_path)


root = Tk()

root.geometry('800x450')
root.eval('tk::PlaceWindow . center')
root.title("tkinter test")
# root.iconbitmap('steve.ico')
# root.iconbitmap(rcpath('steve.ico'))
root.iconbitmap('/Users/hansenlj/Documents/personal/python/steve.ico')
# root.iconbitmap('@'+rcpath('steve.ico'))

myLabel1 = Label(root, text="Hello World!")
myLabel1.pack()

myLabel2 = Label(root, text="My name is Joshua Hansen")
myLabel2.pack()

input = Entry(root)
input.pack()

def solve(text):
  response = Label(root, text=f'Hello {text}')
  response.pack()

buttonUpper = Button(root, text="lower", command=lambda: solve(input.get().lower()))
buttonUpper.pack()

buttonLower = Button(root, text="upper", command=lambda: solve(input.get().upper()))
buttonLower.pack()

root.mainloop()
