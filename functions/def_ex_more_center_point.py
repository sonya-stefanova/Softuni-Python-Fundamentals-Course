import math


def calc_closest_point(a, b, c, d):
    first_distance = 0
    second_distance = 0
    first_distance = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    second_distance = math.sqrt(math.pow(c, 2) + math.pow(d, 2))
    if first_distance < second_distance:
        return f"({a}, {b})"
    elif second_distance < first_distance:
        return f"({c}, {d})"
    elif second_distance == first_distance:
        return f"({a}, {b})"


х1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(calc_closest_point(math.floor(х1), math.floor(y1), math.floor(x2), math.floor(y2)))
