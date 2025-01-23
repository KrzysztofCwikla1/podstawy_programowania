
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        if self.is_on and 1 <= new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
        elif not self.is_on:
            print("TV is off. Turn it on to change the channel.")

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for idx, channel in enumerate(self.channels, 1):
                print(f"{idx}. {channel}")
        else:
            print("No channels available.")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def show_status(self):
        if self.is_on:
            channel_name = (f" ({self.channels[self.channel_no - 1]})"
                            if self.channel_no <= len(self.channels) else "")
            print(f"TV is on, channel {self.channel_no}{channel_name}, volume {self.volume}")
        else:
            print("TV is off.")
