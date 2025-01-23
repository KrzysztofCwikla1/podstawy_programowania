class Phone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def use_app(self, app_name):
        if self.is_on and self.battery_percentage > 0:
            self.battery_percentage -= 10
            print(f"Using {app_name}. Battery at {self.battery_percentage}%.")
        elif not self.is_on:
            print("The phone is OFF. Turn it on first.")
        else:
            print("Battery is dead. Charge your phone.")


def main():
    my_phone = Phone("Samsung", "A53", 74)
    my_phone.power_on()
    my_phone.use_app("Instagram")
    my_phone.use_app("YouTube")
    my_phone.power_off()


if __name__ == "__main__":
    main()
