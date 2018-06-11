# PyJsonAssert

This project aims to be a library for facilitating API testing.

## Reason to be

I've been trying to find a library for testing APIs in python, which in my point of view requires to compare expected jsons with given jsons, as libraries like [PHP Matcher](https://github.com/coduo/php-matcher) or [JSONassert](https://github.com/skyscreamer/JSONassert) do.
My impossibility to find a library with these features, encourage me to do my own.

## Functionality

```
from pyjsonassert import json_assert

expected = {"animal": "dog"}
current = {"animal": "cat"}

# Will fail
json_assert(expected, current)

```

You can also use some flags for strict comparison:

```
from pyjsonassert import json_assert

expected = {"animal": "dog", "place": "home"}
current = {"animal": "dog", "object": "table"}

# Will assert
json_assert(expected, current, allow_unexpected_fields=True, allow_missing_fields=False)
```

## TODO
* Add custom message parameter in the assertion
* Enable patterns for being able to match types, besides the exact value (like [PHP Matcher patterns](https://github.com/coduo/php-matcher#available-patterns))