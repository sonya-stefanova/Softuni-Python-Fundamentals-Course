def lenght_validator(txt: str):
    is_valid = True
    if len(txt)>=6 and len(txt)<=10:
        return True
    print("Password must be between 6 and 10 characters")
    return False

def symbols_validator(txt):
    if not txt.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False

def digits_validator(txt):
    counter = 0
    for each_char in txt:
        if each_char.isdigit():
            counter+=1
    if counter>=2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
validated = [lenght_validator(some_password), \
             symbols_validator(some_password), \
             digits_validator(some_password)]
if all(validated):
    print("Password is valid")
