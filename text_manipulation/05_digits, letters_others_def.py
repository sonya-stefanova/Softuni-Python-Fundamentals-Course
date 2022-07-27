def get_ditits(word):
    return ''.join([str(ch) for ch in word if ch.isdigit()])
def get_letters(word):
    return ''.join([ch for ch in word if ch.isalpha()])
def get_symbols(word):
    return ''.join([ch for ch in word if not ch.isalpha() and not ch.isdigit()])



word = input()  #Agd#53Dfg^&4F53
print(get_ditits(word))
print(get_letters(word))
print(get_symbols(word))
