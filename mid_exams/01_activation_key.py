raw_activation_key = input()
command = input()
if command != "Generate":
    string = command
    if "Contains>>>" in string:
        print(f"{raw activation key} contains {substring}")
        