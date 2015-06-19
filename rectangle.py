class Rectangle():
    def __init__(self,height=2, width=2):
        self.height = height
        self.width = width
    def setHeight(self, height):
        self.height = height
    def setWidth(self, width):
        self.width = width

    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width

    def getArea(self):
        area = self.height * self.width
        return area

    area = property(fget = getArea)

    def getPerimeter(self):
        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter

    perimeter = property(fget = getPerimeter)

    def getStats(self):
        print("Width:     {}".format(self.width))
        print("Height:    {}".format(self.height))
        print("Area:      {}".format(self.area()))
        print("Perimeter: {}".format(self.perimeter()))

def main():
   print "Rectangle a:"
   a = Rectangle(5, 7)
   print "area: %d" % a.area
   print "perimeter: %d" % a.perimeter

   print ""
   print "Rectangle b:"
   b = Rectangle()
   b.width = 10
   b.height = 20
   print b.getStats()

main()
