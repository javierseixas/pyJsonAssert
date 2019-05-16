import unittest
from pyjsonassert import patterns


class TestJsonAssert(unittest.TestCase):

    string = "asfasdf"
    number_as_string = "12"
    number = 12
    float = 12.2
    boolean = False

    uuid = "ba65edf1-3952-40be-b816-c917d46c9078"
    bad_uuid = "ba65edf1-3952-40be-b86-c917d46c907"

    def test_should_identify_an_string(self):

        assert patterns.is_string(self.string) is True

    def test_should_consider_string_a_number_that_comes_as_string_type(self):

        assert patterns.is_string(self.number_as_string) is True

    def test_should_return_false_if_varible_is_not_and_string(self):

        assert patterns.is_string(self.number) is False
        assert patterns.is_string(self.float) is False
        assert patterns.is_string(self.boolean) is False

    def test_should_identify_an_uuid(self):

        assert patterns.is_uuid(self.uuid) is True

    def test_should_return_false_if_uuid_has_wrong_format(self):

        assert patterns.is_uuid(self.bad_uuid) is False
