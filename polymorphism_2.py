from polymorphism import Rectangle, Square, Circle

rect_1 = Rectangle (3,4)
rect_2 = Rectangle (12,5)

print(rect_1.get_area())
print(rect_2.get_area())

squ_1 = Square (5)
squ_2 = Square (10)

print(squ_1.get_area_square(), squ_2.get_area_square())

circ_1 = Circle (6)
circ_2 = Circle (11)

print(circ_1.get_area_circle(), circ_2.get_area_circle())

figures = [rect_1, rect_2, squ_1, squ_2, circ_1, circ_2]

for figure in figures:
    if isinstance(figure,Square):
        print (figure.get_area_square())
    elif isinstance(figure,Circle):
        print (figure.get_area_circle())
    else:
        print(figure.get_area())