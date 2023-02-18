
import math
from Shapes import Polygon


class Shape3D:
    def GetSurfaceArea(self) -> float:
        raise NotImplementedError()

    def GetVolume(self) -> float:
        raise NotImplementedError()


class Cuboid(Shape3D):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def GetVolume(self) -> float:
        return self.length * self.width * self.height

    def GetSurfaceArea(self) -> float:
        return 2 * ((self.length * self.height) + (self.width * self.height) + (self.length * self.width))
    

class Cube(Cuboid):
    def __init__(self, side_length):
       
        super().__init__(side_length, side_length, side_length)

    def GetVolume(self) -> float:
        return super().GetVolume()
    
    def GetSurfaceArea(self) -> float:
        return super().GetSurfaceArea()



class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.height = height
        self.radius = radius

    def _GetBaseArea(self) -> float:
        return math.pi * math.pow(self.radius, 2)

    def GetSurfaceArea(self) -> float:
        return 2 * math.pi * self.radius * (self.height + self.radius)

    def GetVolume(self) -> float:
        return self._GetBaseArea() * self.height
    

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def GetSurfaceArea(self) -> float:
        return 4 * math.pi * math.pow(self.radius, 2)

    def GetVolume(self) -> float:
        return (4/3) * math.pi * math.pow(self.radius, 3)
    

class Prism(Shape3D):
    def __init__(self, side_length, faces, height):
        self.polybase = Polygon(side_length, faces)
        self.height = height
        self.area = (self.polybase.GetArea() * 2) + (self.polybase.GetPerimeter() * self.height)
        self.volume = self.polybase.GetArea() * self.height

    def GetSurfaceArea(self) -> float:
        return self.area

    def GetVolume(self) -> float:
        return self.volume
