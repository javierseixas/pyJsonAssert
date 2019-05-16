import re


class StringMatcher(object):

    pattern = "@string@"

    @classmethod
    def match(self, value):
        return (type(value) == str or type(value) == unicode) and not not re.search(r"^.+$", value)
