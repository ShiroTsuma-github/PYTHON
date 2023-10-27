from math import exp


class IntObl():
    def __init__(self,
                 discretization=1,
                 startRange=0,
                 endRange=100,
                 dimenions=2):
        self.discretization = discretization
        self.startRange = startRange
        self.endRange = endRange
        self.FullRange = startRange - endRange + 1
        self.dimensions = dimenions
        self.Values = np.zeros(
            (int(self.FullRange / self.discretization),
             self.dimensions))

    @staticmethod
    def triangle(x, a, x0, b):
        try:
            if x > a and x <= x0:
                return (x - a) / (x0 - a)
            elif x >= x0 and x <= b:
                return (b - x) / (b - x0)
            return 0
        except ZeroDivisionError:
            return 0

    @staticmethod
    def trap(x, a, x1, x2, b):
        try:
            if x >= a and x <= x1:
                return (x - a) / (x1 - a)
            elif x >= x1 and x <= x2:
                return 1
            elif x >= x2 and x <= b:
                return (b - x) / (b - x2)
            return 0
        except ZeroDivisionError:
            return 0

    @staticmethod
    def singleton(x, x0):
        return 1 if x == x0 else 0

    @staticmethod
    def gauss(x, x0, sigma):
        return exp(-(1/2) * ( (x - x0) / sigma)**2 )