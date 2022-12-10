import unittest

from day6.signal_stream import SignalStream


class SignalStreamPacketStartPositionTest(unittest.TestCase):
    def test_sample_case_1(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_packet_position())

    def test_sample_case_2(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_packet_position())

    def test_sample_case_3(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_packet_position())

    def test_sample_case_4(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_packet_position())


class SignalStreamPacketMessagePositionTest(unittest.TestCase):
    def test_sample_case_1(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_message_position())

    def test_sample_case_2(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_message_position())

    def test_sample_case_3(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_message_position())

    def test_sample_case_4(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_message_position())

    def test_sample_case_5(self):
        signal_stream = SignalStream("INPUT REMOVED AS PER AOC RULES")
        self.assertEqual(0, signal_stream.get_start_message_position())


if __name__ == '__main__':
    unittest.main()
