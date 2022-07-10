pokemons = list(map(int, input().split(" ")))
captured_pokemon = 0

while pokemons>0:
    index = int(input())
    if index>0:
        removed_value = pokemons.pop(index)
        for value in pokemons:
            if value<= removed_value:
                value+=removed_value
            elif value>removed_value:
                value-=removed_value
    elif index<=0

print(captured_pokemon)