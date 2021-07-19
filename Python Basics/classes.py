#class is a imp concept
#it is used to define new types to model real concepts
#NAMING FOR CLASSES IS DONE DIFFRENTLY WE WRITE A CLASS NAME WITH FIRST LETTER IN CAPS.
#IN NAMING DONOT USE UNDERSCORE JUST CAPITALIZE FIRST LETTER OF EACH WORD
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)