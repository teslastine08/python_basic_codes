from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title("Calculator")
calculator.resizable(0, 0)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.creatWigets()

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)
        
    def calculateExpression(self):
        self.Expression = self.display.get()
        self.Expression = self.Expression.replace("%","/ 100")
        self.Expression = self.Expression.replace("^"," ** ")
        
        try:
            
            self.result = eval(self.Expression)
            self.replaceText(self.result)

        except:
            messagebox.showinfo("Error", "invalid input")

        
        
    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
            
        
        else:
            self.display.insert(self.textLength, text)

            
                
    def clearText(self):
            self.replaceText("0")
        
        
        
    def creatWigets(self):
        self.display = Entry(self, font=("Arial Narrow",25), justify=RIGHT, borderwidth=8)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        self.sevenButton = Button(self, bg="light grey", font=("Helvertica",11), text="7", borderwidth=2, command = lambda: self.appendToDisplay("7"))
        self.sevenButton.grid(row=1, column=0, sticky="NENWSESW")

        self.eightButton = Button(self,bg="light grey", font=("Helvertica",11), text="8", borderwidth=2, command = lambda: self.appendToDisplay("8"))
        self.eightButton.grid(row=1, column=1, sticky="NENWSESW")

        self.nineButton = Button(self,bg="light grey", font=("Helvertica",11), text="9", borderwidth=2, command = lambda: self.appendToDisplay("9"))
        self.nineButton.grid(row=1, column=2, sticky="NENWSESW")

        self.timeButton = Button(self, bg="light grey",font=("Helvertica",11), text="*", borderwidth=2, command = lambda: self.appendToDisplay("*"))
        self.timeButton.grid(row=1, column=3, sticky="NENWSESW")

        self.clearButton = Button(self,bg="light grey", font=("Helvertica",11), text="C", borderwidth=2, command = lambda: self.clearText())
        self.clearButton.grid(row=1, column=4, sticky="NENWSESW")

        self.fourButton = Button(self, bg="light grey",font=("Helvertica",11), text="4", borderwidth=2, command = lambda: self.appendToDisplay("4"))
        self.fourButton.grid(row=2, column=0, sticky="NENWSESW")

        self.fiveButton = Button(self,bg="light grey", font=("Helvertica",11), text="5", borderwidth=2, command = lambda: self.appendToDisplay("5"))
        self.fiveButton.grid(row=2, column=1, sticky="NENWSESW")

        self.sixButton = Button(self, bg="light grey",font=("Helvertica",11), text="6", borderwidth=2, command = lambda: self.appendToDisplay("6"))
        self.sixButton.grid(row=2, column=2, sticky="NENWSESW")

        self.divideButton = Button(self,bg="light grey", font=("Helvertica",11), text="/", borderwidth=2, command = lambda: self.appendToDisplay("/"))
        self.divideButton.grid(row=2, column=3, sticky="NENWSESW")

        self.percentageButton = Button(self, bg="light grey",font=("Helvertica",11), text="%", borderwidth=2, command = lambda: self.appendToDisplay("%"))
        self.percentageButton.grid(row=2, column=4, sticky="NENWSESW")

        self.oneButton = Button(self, bg="light grey",font=("Helvertica",11), text="1", borderwidth=2, command = lambda: self.appendToDisplay("1"))
        self.oneButton.grid(row=3, column=0, sticky="NENWSESW")

        self.twoButton = Button(self, bg="light grey",font=("Helvertica",11), text="2", borderwidth=2, command = lambda: self.appendToDisplay("2"))
        self.twoButton.grid(row=3, column=1, sticky="NENWSESW")

        self.threeButton = Button(self, bg="light grey",font=("Helvertica",11), text="3", borderwidth=2, command = lambda: self.appendToDisplay("3"))
        self.threeButton.grid(row=3, column=2, sticky="NENWSESW")

        self.addButton = Button(self, bg="light grey",font=("Helvertica",11), text="+", borderwidth=2, command = lambda: self.appendToDisplay("+"))
        self.addButton.grid(row=3, column=3, sticky="NENWSESW")

        self.minusButton = Button(self, bg="light grey",font=("Helvertica",11), text="-", borderwidth=2, command = lambda: self.appendToDisplay("-"))
        self.minusButton.grid(row=3, column=4, sticky="NENWSESW")

        self.zeroButton = Button(self, bg="light grey",font=("Helvertica",11), text="0", borderwidth=2, command = lambda: self.appendToDisplay("0"))
        self.zeroButton.grid(row=4, column=0, sticky="NENWSESW")

        self.dotButton = Button(self, bg="light grey",font=("Helvertica",11), text=".", borderwidth=2, command = lambda: self.appendToDisplay("."))
        self.dotButton.grid(row=4, column=1, sticky="NENWSESW")

        self.equalsButton = Button(self, bg="light grey",font=("Helvertica",11), text="=", borderwidth=2, command = lambda: self.calculateExpression())
        self.equalsButton.grid(row=4, column=3,columnspan=2, sticky="NENWSESWEW")

        self.squareButton = Button(self, bg="light grey",font=("Helvertica",11), text="^", borderwidth=2, command = lambda: self.appendToDisplay("^"))
        self.squareButton.grid(row=4, column=2, sticky="NENWSESW")

        
        
app = Application(calculator).grid()
calculator.mainloop()
