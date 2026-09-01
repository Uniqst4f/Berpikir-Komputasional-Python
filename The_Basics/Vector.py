import math

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

def main():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(1, 5)

    v2 = v3 + v2
    v1 = v1 * 3
    v4 = v1 *  v3

    print(v2)
    print(abs(v2))
    print(v1)
    print(v4)

if __name__  == "__main__":
    main()



