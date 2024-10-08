import app

# import pytest


def test_add(x, y):
    assert app.add(2, 3) == 5
    assert app.add(1, 2) == 3


def test_subtract(a, b):
    assert app.subtract(3, 0) == 3
    assert app.subtract(10, 5) == 5
