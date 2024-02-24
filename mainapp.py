class Area:
    def __init__(self, circle, square, rectangle):
        self.circle = circle
        self.square = square
        self.rectangle = rectangle

    def circle_area():
        rad = int(input("Enter the radius of the circle: "))
        area = print(f'The area of your circle is {3.14159 * rad * rad}')
        return area
    
    def square_area():
        side = int(input("Enter the measure of the side of your square here: "))
        area = print(f'The are of your square is {side * side}')
        return area

    def rectangle_area():
        length = int(input("Enter the measurement of the long side of your rectangle: "))
        width = int(input("Enter the measurement of the wide side of your rectangle: "))
        print(f'The area of your rectangle is {length * width}')
        return length * width

circle = Area
square = Area
rectangle = Area


ques = input("What shape do you want (C, S, R) > ").lower()

if ques == "c":
    circle.circle_area()

elif ques == "s":
    square.square_area()

elif ques == "r":
    rectangle.rectangle_area()
