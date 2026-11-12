import math

def area(radius):
    """Find area of circle"""
    return math.pi * radius ** 2

def circumference(radius):
    """Find circumference of circle"""
    return 2 * math.pi * radius

if __name__ == '__main__':
    print(area(2))
    print(circumference(4))