import unittest
from pyjsonassert.matchers import StringMatcher


class TestStringMatcher(unittest.TestCase):

    string = "asfasdf"
    number_as_string = "12"
    number = 12
    float = 12.2
    boolean = False

    uuid = "ba65edf1-3952-40be-b816-c917d46c9078"
    bad_uuid = "ba65edf1-3952-40be-b86-c917d46c907"

    def test_should_identify_an_string(self):

        assert StringMatcher.match(self.string) is True

    def test_should_consider_string_a_number_that_comes_as_string_type(self):

        assert StringMatcher.match(self.number_as_string) is True

    def test_should_return_false_if_varible_is_not_and_string(self):

        assert StringMatcher.match(self.number) is False
        assert StringMatcher.match(self.float) is False
        assert StringMatcher.match(self.boolean) is False