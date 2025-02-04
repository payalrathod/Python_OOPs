class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


r1 = Rectangle(10, 20)
print(r1.width)

r1.width = 25
print(r1.width)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r1 = Rectangle(11, 2)
print(r1.area())
print(r1.perimeter())

print(str(r1))
print(hex(id(r1)))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        print('Rectangle: width={0}, height={1}'.format(self.width, self.height))

    # def __repr__(self):
    #     print('Rectangle({0}, {1})'.format(self.width, self.height))

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(4, 2)

# print(str(r1))
# print(r1.to_string())
r2 = Rectangle(4, 3)

print(r1 == r2)
print(r1 == 100)
print(r1 < r2)


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError
        else:
            self._width = width

    def __str__(self):
        print('Rectangle: width={0}, height={1}'.format(self._width, self.height))

    # def __repr__(self):
    #     print('Rectangle({0}, {1})'.format(self.width, self.height))

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self.height) == (other._width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(2,3)

print(r1.get_width())
# r1.set_width() = -100  -> incorrect
print(r1.set_width(100))


