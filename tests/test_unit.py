from main import add, subtract

def test_add():
    assert add(10, 5)["result"] == 15


def test_subtract():
    assert subtract(20, 8)["result"] == 12


