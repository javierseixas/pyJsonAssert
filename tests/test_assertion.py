import unittest
from pyjsonassert import assert_json


class TestJsonAssert(unittest.TestCase):
    json_1 = {"animal": "dog"}
    json_2 = {"animal": "cat"}
    json_3 = {"animal": "dog", "object": "table"}
    json_string_pattern = {"animal": "@string@"}

    json_complex_1 = {"animal": {
        "paws": 4,
        "color": "black"
    }}
    json_complex_2 = {"animal": {
        "paws": 4,
        "color": "white"
    }}
    json_complex_string_pattern = {"animal": {
        "paws": 4,
        "color": "@string@"
    }}

    json_very_complex_1 = {"animal": {
        "eyes": {
            "color": "blue"
        }
    }}
    json_very_complex_2 = {"animal": {
        "eyes": {
            "color": 2
        }
    }}
    json_very_complex_string_pattern = {"animal": {
        "eyes": {
            "color": "@string@"
        }
    }}

    json_str_1 = "{\"animal\": \"dog\"}"
    json_str_2 = "{\"animal\": \"cat\"}"
    json_str_3 = "{\"animal\": \"dog\", \"object\": \"table\"}"

    def test_it_should_assert_when_jsons_are_equal(self):

        assert_json(self.json_1, self.json_1)
        assert_json(self.json_str_1, self.json_str_1)
        assert_json(self.json_complex_1, self.json_complex_1)

    def test_it_should_fail_when_jsons_have_same_key_and_different_value(self):

        self.assertRaises(Exception, assert_json, self.json_1, self.json_2)
        self.assertRaises(Exception, assert_json, self.json_str_1, self.json_str_2)
        self.assertRaises(Exception, assert_json, self.json_complex_1, self.json_complex_2)

    def test_it_should_assert_when_jsons_match_one_key_but_current_json_contains_another_key_value(self):

        assert_json(self.json_1, self.json_3)
        assert_json(self.json_str_1, self.json_str_3)

    def test_it_should_fail_when_jsons_match_one_key_but_one_contains_another_key_value_and_not_new_value_are_accepted(self):

        self.assertRaises(Exception, assert_json, self.json_1, self.json_3, False)
        self.assertRaises(Exception, assert_json, self.json_str_1, self.json_str_3, False)

    def test_it_should_fail_when_expected_json_has_more_keys_than_current_json(self):

        self.assertRaises(Exception, assert_json, self.json_3, self.json_1)
        self.assertRaises(Exception, assert_json, self.json_str_3, self.json_str_1)

    def test_it_should_assert_when_expected_json_has_more_keys_than_current_json_and_it_is_allowed(self):

        assert_json(self.json_3, self.json_1, True, True)
        assert_json(self.json_str_3, self.json_str_1, True, True)

    # Testing patterns

    def test_it_should_assert_when_using_string_pattern(self):

        assert_json(self.json_string_pattern, self.json_1)
        assert_json(self.json_complex_string_pattern, self.json_complex_1)
        assert_json(self.json_very_complex_string_pattern, self.json_very_complex_1)

    def test_it_should_fail_when_using_string_pattern_compares_with_a_number(self):

        self.assertRaises(Exception, assert_json, self.json_very_complex_string_pattern, self.json_very_complex_2)


if __name__ == '__main__':
    unittest.main()
