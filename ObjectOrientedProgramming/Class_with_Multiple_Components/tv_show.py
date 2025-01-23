
from tv import TV

def main():
    tv = TV()

    print("Show TV status:")
    tv.show_status()

    print("\nTurn TV on:")
    tv.turn_on()
    tv.show_status()

    print("\nSet channels:")
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    tv.show_channels()

    print("\nChange to channel 4:")
    tv.set_channel(4)
    tv.show_status()

    print("\nIncrease volume to 5:")
    for _ in range(5):
        tv.increase_volume()
    tv.show_status()

    print("\nTurn TV off:")
    tv.turn_off()
    tv.show_status()

if __name__ == "__main__":
    main()

