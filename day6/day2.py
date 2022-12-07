from day6.signal_stream import SignalStream


def main():
    with open('input', 'r') as file:
        data = file.read().strip()
        signal_stream = SignalStream(data)
        print(signal_stream.get_start_message_position())


if __name__ == "__main__":
    main()
