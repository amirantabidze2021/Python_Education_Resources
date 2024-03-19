class Rectangle :
    """
    Docstring type here 
    
    """
    def __init__(self,width=6, length=7):          
        self.width = width
        self.length = length
    def perimeter (self):
        return 2*(self.width + self.length)
    
obj1 = Rectangle(5,5)
#obj1 = Rectangle(3,5)
print(obj1.perimeter())
#print(obj1.length)
#print(Rectangle.perimeter(obj1))



