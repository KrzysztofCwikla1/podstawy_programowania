celcius = float(input("Temperature in Celcius: "))

#conversion from celcius to fahrenheit degrees
fahrenheit = (9/5) * celcius + 32
print(f"{celcius} degrees in Celcius is {fahrenheit:.2f} degrees in fahrenheit")


#conversion from celcius to kelvin degrees
kelvin = celcius + 273.15
print(f"{celcius} degrees in Celcius is {kelvin:.2f} degrees in kelvin")