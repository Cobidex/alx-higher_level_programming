#!/usr/bin/python3
"""""This module create a rectangle"""


class Rectangle:
    """
    class that generate a rectangle
    """

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Constructor initialize the class rectangle
        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter function of width
        Returns:
            int -- width fo the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function to width
        Arguments:
            value {int} -- [valeu of width]
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter function to height
        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function os height
        Arguments:
            value {int} -- Value of height
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """calculates the area of rectangle

        Returns:
            Calculated area
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter

        Return:
            0 or perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """specifies behaviour of print"""

        str_ptr = ""
        if self.width == 0 or self.height == 0:
            return str_ptr
        else:
            for i in range(self.height):
                for j in range(self.width):
                    str_ptr += "#"
                if i < (self.height - 1):
                    str_ptr += "\n"
        return str_ptr

    def __repr__(self):
        """returns object string"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """deletes a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
