initial_version = [int(number) for number in input().split('.')]
initial_version[-1]+=1
for current_index in range(len(initial_version)-1, -1, -1):
    if initial_version[current_index]>9:
        initial_version[current_index]=0
        if current_index-1>=0:
            initial_version[current_index-1]+=1
print(".".join(str(number) for number in initial_version))
