import math

class Counter():
    """counter."""
    def __init__(self):
       self.x = 0
    def increase(self):
     self.x = self.x + 1
    def increments(self):
         return self.x
    def toString(self):
      print str(self.x)
class Punto2D():
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return x

    def get_y(self):
      return y

    def radio_polar(self):
        return math.sqrt((get_x**2) + (get_y**2))
    def angulo_polar(self):
       return math.atan(x/y)
    def dist_euclidiana(self, Punto2D other):
        dx = self.x - other.get_x()
        dy = self.y - other.get_y()
        return math.sqrt((dx*dx)+(dy*dy))
