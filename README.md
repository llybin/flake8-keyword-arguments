# flake8-keyword-arguments

___

A flake8 extension that is looking for function calls and forces to use keyword arguments if there are more than X (default=2) arguments

Fork for python 2.7


## Installation

```
pip install flake8-keyword-arguments
```

## Example

```python
def one_argument(one):
    pass


def two_arguments(one, two):
    pass


def multiple_arguments(one, two, three):
    pass


one_argument(1)
one_argument(one=1)
two_arguments(1, 2)
two_arguments(one=1, two=2)
multiple_arguments(one=1, two=2, three=3)
multiple_arguments(1, 2, 3)
```

Usage:

```terminal
$ flake8 test.py
test.py:18: [FKA01] multiple_arguments's call uses 3 positional arguments, use keyword arguments.

$ flake8 test.py --max-pos-args=1
test.py:15: [FKA01] two_arguments's call uses 2 positional arguments, use keyword arguments.
test.py:18: [FKA01] multiple_arguments's call uses 3 positional arguments, use keyword arguments.
```

Tested on Python 2.7

## Error codes

| Error code |                     Description                                |
|:----------:|:--------------------------------------------------------------:|
|   FKA01    | XXX's call uses N positional arguments, use keyword arguments. |


## Options
| Option             |                     Description                        |
|:------------------:|:------------------------------------------------------:|
|   --max-pos_args   | How many positional arguments are allowed (default: 2) |
