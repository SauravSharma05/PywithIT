#encapsulation
class Sensor:
      def __init__(self, name, location):
            self.name = name
            self._location = location
            self.__version = '1.0'

      def get_version(self):
            return f'The sensor version is {self.__version}'

      def set_version(self, version):
            self.__version = version
            sensor1 = Sensor('TemperatureSensor', 'Room1')
            print(sensor1.name)
            print(sensor1._location)
            print(sensor1.get_version())
            sensor1.set_version('2.0')
            print(sensor1.get_version())




#inheritance
class Accelerometer:
      def __init__(self, name):
            self.name = name

      def show_type(self):
            print(f'I am an accelerometer named {self.name}')

class UCBAcc(Accelerometer):
      def show_type(self):
            print(f'I am {self.name}, created at UC Berkeley!')acc_ucb =                   UCBAcc('UCBAcc')acc_ucb.show_type()


#polymorphism
class Shape:
def area(self):

class Circle(Shape):
      def __init__(self, radius):
            self.radius = radius

      def area(self):
            return 3.14 * (self.radius ** 2)

class Square(Shape):
      def __init__(self, side):
            self.side = side

      def area(self):
            return self.side ** 2shapes = [Circle(5), Square(4)]
            for shape in shapes: print(f'Area: {shape.area()}')



# abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")


