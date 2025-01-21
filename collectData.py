class Circle:
    pi = 3.142
    
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def calculate_circumference(cls, radius):
        return 2* cls.pi * radius
    
print(Circle.calculate_circumference(5))