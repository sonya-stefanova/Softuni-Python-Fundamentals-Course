line = input()
new_line = ""

for el in range(len(line)-1): #дължината ще е -1, защото иначе ще минем в out of index
    if line[el] != line[el+1]:
        new_line += line[el]

new_line += line[-1]#последното не можем да сравним с нищо, затова директно го добаявме

print(new_line)