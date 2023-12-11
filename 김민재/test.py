x = {1: 1, 2: 1}

def test(z):
    x = 1
    y = 2
    def yes():
        nonlocal x, y, z
        x += 1
        y += 1
        z += 1
        print(x, y, z)
    yes()


test(5)