def add(x,  y):
    return x + y

def subtract(x, y):
    return x + y

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(1, -1) == 0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(3, 10) == -7

if __name__ == "__main__":
    print(add(3, 12))
    print(subtract(12,3))