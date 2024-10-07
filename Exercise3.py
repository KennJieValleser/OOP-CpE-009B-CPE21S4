from tkinter import*

class MyWindow:
    def __init__(self, win):
        #common widgets
        self.Label1=Label(win, fg="Black", text="Calculator", bg="bisque", font=("Times New Roman", 24) )
        self.Label1.place(x=140,y=10)

        self.Label2=Label(win, text="Number 1: ", bg="bisque")
        self.Label2.place(x=50,y=70)

        self.Entry1=Entry(win, bd=5)
        self.Entry1.place(x=150,y=70)

        self.Label3 = Label(win, text="Number 2: ", bg="bisque")
        self.Label3.place(x=50, y=110)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=150, y=110)

        self.Label4 = Label(win, text="Result: ", bg="bisque")
        self.Label4.place(x=50, y=150)

        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=150, y=150)

        self.Button1=Button(win,fg="White",text="Add", bg="Green",command=self.add)
        self.Button1.place(x=80,y=200)
        self.Button1.bind('<Button-1>',self.add)

        self.Button2 = Button(win, fg="White", text="Subtract", bg="Red",command=self.subtract)
        self.Button2.place(x=130, y=200)

        self.Button3 = Button(win, fg="White", text="Multiply", bg="Blue",command=self.multiply)
        self.Button3.place(x=200, y=200)

        self.Button4 = Button(win, fg="White", text="Divide", bg="Magenta",command=self.divide)
        self.Button4.place(x=270, y=200)

        win.config(bg="bisque")

    def add(self):
        self.Entry3.delete(0,'end')
        num1=int(self.Entry1.get())
        num2=int(self.Entry2.get())
        result=num1 + num2
        self.Entry3.insert(END,str(result))

    def subtract(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))


    def multiply(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))


    def divide(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))


window=Tk()
MyWin=MyWindow(window)
window.geometry("400x500+10+10")
window.title("Standard Calculator")
window.mainloop()

