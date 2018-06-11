import unittest
from pyjsonassert.do import assert_json


class TestInvert(unittest.TestCase):
    json_1 = {"animal": "dog"}
    json_2 = {"animal": "dog"}
    json_3 = {"animal": "cat"}
    json_4 = {"animal": "dog", "object": "table"}

    def test_it_should_assert_when_jsons_are_equal(self):

        assert_json(self.json_1, self.json_2)

    def test_it_should_fail_when_jsons_have_same_key_and_different_value(self):

        self.assertRaises(Exception, assert_json, self.json_1, self.json_3)

    def test_it_should_assert_when_jsons_match_one_key_but_one_contains_another_key_value(self):

        assert_json(self.json_1, self.json_4)




if __name__ == '__main__':
    unittest.main()
