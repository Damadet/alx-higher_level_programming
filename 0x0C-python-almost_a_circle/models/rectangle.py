from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id = None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y



    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <=0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <=0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        print("Retrieving the value of x")
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value <=0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    
    @property
    def y(self):
        print("Retrieving the value of y")
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value <=0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value
