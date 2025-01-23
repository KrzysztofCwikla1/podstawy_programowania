
import random

class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            temp = round(random.uniform(34.0, 42.0), 1)
            status = f"Temperature: {temp}C"
            if temp >= 41.0:
                status += " (CRITICAL TEMPERATURE!!)"
            elif temp >= 37.0:
                status += " (fever)"
            print(status)
        else:
            print("Thermometer is off.")


def main():
    thermo = Thermometer()

    print("Turn thermometer on:")
    thermo.turn_on()

    print("\nMeasure temperature:")
    thermo.measure()

    print("\nTurn thermometer off:")
    thermo.turn_off()

if __name__ == "__main__":
    main()
