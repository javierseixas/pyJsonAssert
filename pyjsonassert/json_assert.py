from jsondiff import diff
from pyjsonassert.matchers import *
import json

matchers = {
    "@string@": StringMatcher(),
    "@uuid@": UuidMatcher()
}


def resolve_matcher(pattern):
    return matchers[pattern]


def has_matcher(pattern):
    return pattern in matchers


def assert_json(expected_json, current_json, allow_unexpected_fields=True, allow_missing_fields=False):

    if isinstance(expected_json, str):
        expected_json = json.loads(expected_json)

    if isinstance(current_json, str):
        current_json = json.loads(current_json)

    differences = json.loads(diff(expected_json, current_json, syntax='symmetric', dump=True))

    reserved_keynames = ["$delete", "$insert"]

    if not allow_missing_fields:
        if '$delete' in differences:
            raise Exception('Some fields are missing')

    if not allow_unexpected_fields:
        if '$insert' in differences:
            raise Exception('There are fields not expected')

    differences = process_differences_with_patterns(differences)

    copied_differences = differences.copy()

    for keyword in reserved_keynames:
        if keyword in copied_differences:
            del copied_differences[keyword]

    if len(copied_differences) > 0:
        raise Exception('Json documents doesn\'t match: {}'.format(copied_differences))


def process_differences_with_patterns(differences):
    keys_matched_by_pattern = []
    for key, value in differences.items():
        if isinstance(value, dict):
            result = process_differences_with_patterns(value)
            if len(result) == 0:
                keys_matched_by_pattern.append(key)

        elif type(value) == list:
            if has_matcher(value[0]):
                if resolve_matcher(value[0]).match(value[1]):
                    keys_matched_by_pattern.append(key)

    for matched_key in keys_matched_by_pattern:
        differences.pop(matched_key, None)

    return differences
