import math


def calc_longest_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_distance = 0
    second_distance = 0
    third_distance = 0
    forth_distance = 0
    longest_line = ""
    x1y1 = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2))
    x2y2 = math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))
    x3y3 = math.sqrt(math.pow(x3, 2) + math.pow(y3, 2))
    x4y4 = math.sqrt(math.pow(x4, 2) + math.pow(y4, 2))
    distance_first_line = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    distance_second_line = math.sqrt(math.pow(x4 - x3, 2) + math.pow(y4 - y3, 2))
    if distance_first_line >= distance_second_line:
        longest_line = distance_first_line
        if x1y1 < x2y2:
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        elif x1y1 > x2y2:
            return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    else:
        longest_line = distance_second_line
        if x3y3 < x4y4:
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        elif x4y4 < x3y3:
            return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"


х1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
х3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(calc_longest_line(х1, y1, x2, y2, х3, y3, x4, y4))
