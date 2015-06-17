class Rectangle():
    def __init__(self,height=2, width=2):
        self.height = height
        self.width = width
    def setHeight(self, height):
        if type(height)!=int:
            self.height = 2
        else:
            self.height = height
    def setWidth(self, width):
        if type(width)!=int:
            self.width = 2
        else:
            self.width = width

    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width

    def perimeter(self):
        perimeter = ((2*self.height)+(2*self.width))
        return perimeter

    def area(self):
        return self.height * self.width

    def getStats(self):
        print("Width:     {}".format(self.width))
        print("Height:    {}".format(self.height))
        print("Area:      {}".format(self.area()))
        print("Perimeter: {}".format(self.perimeter()))

def main():
    print ("Rectangle a:")
    a = Rectangle(5,7)
    print ("area: {}".format(a.area()))
    print ("perimeter: {}".format(a.perimeter()))
    print ""
    print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    b.getStats()

main()
