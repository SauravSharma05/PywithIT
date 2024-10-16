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