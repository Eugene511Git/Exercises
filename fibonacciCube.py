cube = lambda x: x**3

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for i in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq

print (list(map(cube, fibonacci(10))))
