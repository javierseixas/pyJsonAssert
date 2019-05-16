import unittest
from pyjsonassert.matchers import UuidMatcher


class TestUuidMatcher(unittest.TestCase):

    pattern = "@uuid@"

    uuid = "ba65edf1-3952-40be-b816-c917d46c9078"
    bad_uuid = "ba65edf1-3952-40be-b86-c917d46c907"

    def test_should_identify_an_uuid(self):

        assert UuidMatcher.match(self.uuid) is True

    def test_should_return_false_if_uuid_has_wrong_format(self):

        assert UuidMatcher.match(self.bad_uuid) is False
