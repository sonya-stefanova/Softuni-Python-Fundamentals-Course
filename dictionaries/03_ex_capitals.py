country_names = input().split(", ")
capitals = input().split(", ")
dict_countries_to_letters = dict(zip(country_names, capitals))
geography_representation = [f'{country_name} -> {capitals}' for country_name, capitals in dict_countries_to_letters.items()]
geography_representation = '\n'.join(geography_representation)
print(geography_representation)

# countries = input().split(", ")
# capitals = input().split(", ")
# result = {countries[index] : capitals[index] for index in range(len(countries))}
# # result = dict(zip(countries, capitals))
# for country, capital in result.items():
#     print(f"{country} -> {capital}")