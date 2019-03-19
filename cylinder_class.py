class Cylinder():
    pi=3.14
    def __init__(self,radius=1,height=1):
        self.radius=radius
        self.height=height

    def get_volume(self):
        return self.height*3.14*(self.radius)**2

    def get_surface_area(self):
        top = 3.14 * (self.radius) ** 2
        return (2 * top) + (2 * 3.14 * self.radius * self.height)

c=Cylinder(3,2)
print(c.get_volume())
print(c.get_surface_area())