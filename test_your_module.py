from your_module import add_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5  # nosec

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5  # nosec

