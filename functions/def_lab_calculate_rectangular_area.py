# def rectangular_area(a,b):
#     result = a*b
#     return result

rectangular_area = lambda a, b: a * b

width = int(input())
height = int(input())
result = rectangular_area(width, height)
print(result)
