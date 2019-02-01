from unittest import TestCase

from string_to_int_converter.string_to_int_converter import StringToIntConverter


class StringToIntConverterTests(TestCase):
    def test_one_digit_number(self):
        string_to_convert = "9"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 9)

    def test_two_digit_number(self):
        string_to_convert = "48"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 48)

    def test_three_digit_number(self):
        string_to_convert = "293"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 293)

    def test_10_digit_number(self):
        string_to_convert = "1234567891"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 1234567891)

    def test_number_that_starts_with_0(self):
        string_to_convert = "011"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 11)

    def test_number_with_0_in_middle(self):
        string_to_convert = "101"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 101)

    def test_number_that_ends_with_0(self):
        string_to_convert = "110"
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 110)

    def test_empty_string_converted_to_0(self):
        string_to_convert = ""
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 0)

    def test_None_converted_to_0(self):
        string_to_convert = None
        converter = StringToIntConverter(string_to_convert)
        converted_int = converter.convert()
        self.assertEquals(converted_int, 0)
