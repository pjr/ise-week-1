def add(x,  y):
    return x + y

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(1, -1) == 0

if __name__ == "__main__":
    print(add(3, 12))