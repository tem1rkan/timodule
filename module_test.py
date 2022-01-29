from converter import *

x = int(input())
c = Converter(x)

print(c.meters_to_nanometers(x))
print(c.nanometers_to_meters(x))
    
print(c.meters_to_micrometers(x))
print(c.micrometers_to_meters(x))
  
print(c.meters_to_millimeters(x))
print(c.millimeters_to_meters(x))
  
print(c.meters_to_centimeters(x))
print(c.centimeters_to_meters(x))
    
print(c.meters_to_decimeters(x))
print(c.decimeters_to_meters(x))
    
print(c.meters_to_kilometers(x))
print(c.kilometers_to_meters(x))
   
print(c.meters_to_feet(x))
print(c.feet_to_meters(x))
    
print(c.meters_to_miles(x))
print(c.miles_to_meters(x))

print(c.meters_to_yards(x))
print(c.yards_to_meters(x))
    
print(c.meters_to_inches(x))
print(c.inches_to_meters(x))
    
print(c.celsius_to_fahrenheit(x))
print(c.fahrenheit_to_celsius(x))
    
print(c.celsius_to_kelvin(x))
print(c.kelvin_to_celsius(x))
    
print(c.decimal_to_binary(x))
print(c.binary_to_decimal(x))
