def add_or_increment(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1


class SignalStream:
    def __init__(self, stream: str):
        self.data = stream

    def get_start_position(self, window_size) -> int:
        window = {}
        for i in range(len(self.data)):
            next_chunk = self.data[i]
            if i < window_size:
                add_or_increment(window, next_chunk)
            else:
                removed_chunk = self.data[i - window_size]
                window[removed_chunk] -= 1
                if window[removed_chunk] == 0:
                    del window[removed_chunk]
                add_or_increment(window, next_chunk)
                if all([window[key] == 1 for key in window]):
                    return i + 1
        return -1

    def get_start_packet_position(self):
        return self.get_start_position(4)

    def get_start_message_position(self):
        return self.get_start_position(14)
