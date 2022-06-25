#print(list(map(lambda x: round(float(x)), input().split(" "))))
rounded = [round(float(num)) for num in input().split(" ")]
print(rounded)