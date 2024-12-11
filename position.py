from random import randint

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return NotImplemented
    @staticmethod
    def get_none():
        return Position(-1,-1)
    

    @staticmethod
    def randomPosition(maxX,maxY):
        return Position(randint(0,maxX), randint(0, maxY))
    def __mul__(self, scalar):
        # Multiply the vector by a scalar
        return Position(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        # Reverse multiplication: scalar * vector
        return self.__mul__(scalar)
        
    def __str__(self):
        return f"{self.x},{self.y}"
    
    def __repr__(self):
        return f"{self.x},{self.y}"
    
    def copy(self):
        return Position(self.x, self.y)
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y