class Converter:
    def __init__(self, x):
        self.x = x
    # meters <> nanometers
    def meters_to_nanometers(self, x):
        return x * 1000000000
    def nanometers_to_meters(self, x):
        return x / 1000000000
        
    # meters <> micrometers
    def meters_to_micrometers(self, x):
        return x * 1000000
    def micrometers_to_meters(self, x):
        return x / 1000000

    # meters <> millimeters
    def meters_to_millimeters(self, x):
        return x * 1000
    def millimeters_to_meters(self, x):
        return x / 1000

    # meters <> centimeters
    def meters_to_centimeters(self, x):
        return x * 100
    def centimeters_to_meters(self, x):
        return x / 100
    
    # meters <> decimeters
    def meters_to_decimeters(self, x):
        return x * 10
    def decimeters_to_meters(self, x):
        return x / 10

    # meters <> kilometers
    def meters_to_kilometers(self, x):
        return x / 1000
    def kilometers_to_meters(self, x):
        return x * 1000
        
    # meters <> feet
    def meters_to_feet(self, x):
        return x / 3.280839895013123
    def feet_to_meters(self, x):
        return x * 3.280839895013123
     
    # meters <> miles
    def meters_to_miles(self,x):
        return x / 1609.34
    def miles_to_meters(self,x):
        return x * 1609.34

    # meters <> yards
    def meters_to_yards(self, x):
        return x / 0.9144
    def yards_to_meters(self, x):
        return x * 0.9144

    # meters <> inches
    def meters_to_inches(self, x):
        return x / 0.0254
    def inches_to_meters(self, x):
        return x * 0.0254

    # celsius <> fahrenheit
    def celsius_to_fahrenheit(self, x):
        return (x * 9 / 5) + 32
    def fahrenheit_to_celsius(self, x):
        return (x - 32) * 5 / 9

    # celsius <> kelvin
    def celsius_to_kelvin(self, x):
        return x + 273.15
    def kelvin_to_celsius(self, x):
        return x - 273.15
        
    # decimal <> binary
    def decimal_to_binary(self, x):
        a = ''
        while x > 0:
            a = str(x % 2) + a
            x //= 2
        return a
    def binary_to_decimal(self, x):
        l = len(str(x))
        a = 0
        for i in range(0, l): 
            a = a + int(str(x)[i]) * (2 ** (l - i - 1))  
        return a

    # rgb <> hex
