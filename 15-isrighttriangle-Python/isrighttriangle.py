# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
def distance(x1, y1, x2, y2):
            return (x1-x2)**2 + (y2-y1)**2
def isrighttriangle(x1, y1, x2, y2, x3, y3):
    # your code goes here
    a=distance(x1, y1, x2, y2)
    b=distance(x3, y3, x2, y2)
    c=distance(x1, y1, x3, y3)
    if (a==b+c or b==c+a or c==a+b):
        return True
    return False