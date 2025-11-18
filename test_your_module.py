from your_module import add_numbers, divide_numbers
import pytest

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
