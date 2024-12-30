class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")
        
point = Point(23, 15)
print(point.x, point.y)