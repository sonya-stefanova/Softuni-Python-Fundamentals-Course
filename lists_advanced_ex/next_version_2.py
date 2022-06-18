initial_version = input()
initial_version = int(initial_version.replace(".",""))
next_version = str(initial_version+1)
print(f'{next_version[0]}.{next_version[1]}.{next_version[2]}')