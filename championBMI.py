""" bmi.py
    bmi calculator
"""

from Tkinter import *
#Class for GUI
class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.title("BMI")
    self.lblText = Label(self, text = "BMI CALCULATOR") #H1
    self.lblText.grid(row=0, columnspan=2)
    
    self.lblFeet = Label(self, text = "Height(feet): ") #feet tall
    self.lblFeet.grid(row=1, column=0)
    self.txtFeet = Entry(self)
    self.txtFeet.grid(row=1, column=1)
    
    self.lblInch = Label(self, text = "Height(inches): ") #inches tall
    self.lblInch.grid(row=2, column=0)
    self.txtInch = Entry(self)
    self.txtInch.grid(row=2, column=1)
    
    self.lblWeight = Label(self, text = "WEIGHT(lb): ") #weight
    self.lblWeight.grid(row=3, column=0)
    self.txtWeight = Entry(self)
    self.txtWeight.grid(row=3, column=1)
    
    self.btnButton = Button(self, text = "CALCULATE BMI", command = self.calculate)
    self.btnButton.grid(row=4, columnspan=2) #lets the button stretch cells
  
    self.lblBmi = Label(self, text = "BMI: ") #associated info for output in column2
    self.lblBmi.grid(row=5, column=0)
    
    self.lblStatus = Label(self, text = "STATUS: ")
    self.lblStatus.grid(row=6, column=0)


    self.mainloop()
#calculations
  def calculate(self):
    Feet = float(int(self.txtFeet.get()))
    Inch = float(int(self.txtInch.get()))
    Weight = float(int(self.txtWeight.get()))

    Height = (Feet * 12) + Inch #turns feet into inches and then adds them together

    bmi = float(Weight * 702 / Height**2)
    self.lblBmi = Label(self, text = "%.2f" % bmi) #output for BMI
    self.lblBmi.grid(row=5, column=1)

    if bmi >= 30: #checks BMI range
        Status = "obese"
    elif (bmi >= 25) and (bmi <= 29.9):
        Status = "overweight"
    elif (bmi >= 18.51) and (bmi <= 24.9):
        Status = "normal"
    else:
        Status = "underweight"

    self.lblStatus = Label(self, text = "%s" % Status) #output for status
    self.lblStatus.grid(row=6, column=1)

def main():
  a = App()
  
if __name__ == "__main__":
  main()
