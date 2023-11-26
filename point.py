class Point:

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y) 


    def getX(self):
        return self.X

    def getY(self):
        return self.Y
        
    def getDict(self):
        data = {
            "x": self.X,
            "y": self.Y
        }
        return data
