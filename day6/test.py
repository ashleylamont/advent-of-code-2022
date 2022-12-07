import unittest

from day6.signal_stream import SignalStream


class SignalStreamPacketStartPositionTest(unittest.TestCase):
    def test_sample_case_1(self):
        signal_stream = SignalStream("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(5, signal_stream.get_start_packet_position())

    def test_sample_case_2(self):
        signal_stream = SignalStream("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(6, signal_stream.get_start_packet_position())

    def test_sample_case_3(self):
        signal_stream = SignalStream("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(10, signal_stream.get_start_packet_position())

    def test_sample_case_4(self):
        signal_stream = SignalStream("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(11, signal_stream.get_start_packet_position())


class SignalStreamPacketMessagePositionTest(unittest.TestCase):
    def test_sample_case_1(self):
        signal_stream = SignalStream("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
        self.assertEqual(19, signal_stream.get_start_message_position())

    def test_sample_case_2(self):
        signal_stream = SignalStream("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(23, signal_stream.get_start_message_position())

    def test_sample_case_3(self):
        signal_stream = SignalStream("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(23, signal_stream.get_start_message_position())

    def test_sample_case_4(self):
        signal_stream = SignalStream("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(29, signal_stream.get_start_message_position())

    def test_sample_case_5(self):
        signal_stream = SignalStream("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(26, signal_stream.get_start_message_position())


if __name__ == '__main__':
    unittest.main()
