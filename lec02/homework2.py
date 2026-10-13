
def arithmetic(x,y):
    if isinstance(x, str) and isinstance(y, str):
        return x + y
    elif isinstance(x, float) and isinstance(y,str):
        return str(x) + y
    elif isinstance(x, str) and isinstance(y, float):
        return x * int(y)
    elif isinstance(x, float) and isinstance(y, float):
        return x * y
print(arithmetic("Hello", "Sensei"))
print(arithmetic(3.14, "PiValue"))
print(arithmetic("PiValue", 3.14))
print(arithmetic(1.5, 3.0))

