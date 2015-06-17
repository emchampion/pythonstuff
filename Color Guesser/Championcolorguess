""" colorname.py
name the color game to associate the word with the color
"""
 
from Tkinter import *
import random
 
color = ["red", "blue", "green", "orange", "yellow", "purple"]
 
#Class for GUI
class App(Tk):
  def __init__(self):
    Tk.__init__(self)
#title 
    self.title("Color Match")
    self.lblText = Label(self, text = "Name the Color") #H1
    self.lblText.grid(row=0, columnspan=3)
#generats random color
    self.colorshow()
#buttons  
    self.btnRed = Button(self, text = "Red", command = self.Red)
    self.btnRed.grid(row = 5, column = 0)
 
    self.btnYellow = Button(self, text = "Yellow", command = self.Yellow)
    self.btnYellow.grid(row = 5, column = 1)
 
    self.btnBlue = Button(self, text = "Blue", command = self.Blue)
    self.btnBlue.grid(row = 5, column = 2)
 
    self.btnGreen = Button(self, text = "Green", command = self.Green)
    self.btnGreen.grid(row = 6, column = 0)
 
    self.btnOrange = Button(self, text = "Orange", command = self.Orange)
    self.btnOrange.grid(row = 6, column = 1)
        
    self.btnPurple = Button(self, text = "Purple", command = self.Purple)
    self.btnPurple.grid(row = 6, column = 2)
#generate new color button 
    self.btnGen = Button(self, text = "Generate Color", command = self.colorshow)
    self.btnGen.grid(row = 8, column = 1)
    
    self.mainloop()
#turns the button clicks into inputs
  def Red(self):
    self.guess("red")
    
  def Yellow(self):
    self.guess("yellow")
    
  def Blue(self):
    self.guess("blue")
    
  def Green(self):
    self.guess("green")
    
  def Orange(self):
    self.guess("orange")
 
  def Purple(self):
    self.guess("purple")
 
#random color
  def colorshow(self):
    self.colorPicked = random.choice(color)
    self.lblStatus = Label(self, text = "spacing text spacing text", fg =self.colorPicked, bg =self.colorPicked)
    self.lblStatus.grid(row = 3, columnspan=3)
    self.lblStatus = Label(self, text = "                                                                      " )
    self.lblStatus.grid(row = 4, columnspan=3)
    
#checks to see if the button pressed correlates with the color shown    
  def guess(self, selection):
    newcolor = self.colorPicked
    if  selection == newcolor:
        self.lblStatus = Label(self, text = "Correct! (Generate Color to Continue)")
        self.lblStatus.grid(row = 4, columnspan=3)
    else:
        self.lblStatus = Label(self, text = "Wrong! try again")
        self.lblStatus.grid(row = 4, columnspan=3)
  
def main():
  a = App()
  
if __name__ == "__main__":
  main()
