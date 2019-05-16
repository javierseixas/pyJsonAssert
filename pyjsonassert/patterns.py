import re


def is_string(string):
    return (type(string) == str or type(string) == unicode) and not not re.search(r"^.+$", string)


def is_uuid(uuid):
    return is_string(uuid) and not not re.search(r"^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$", uuid)
