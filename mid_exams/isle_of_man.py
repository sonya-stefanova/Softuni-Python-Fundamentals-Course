save = []
while True:
    text = input()  # SteveHislop#=16!!tv5dekdz8x11ddkc

    if "=" not in text:
        print("Nothing found!")
        continue

    separation = text.split("=")  # ["SteveHislop#", "16!!tv5dekdz8x11ddkc"]
    name = separation[0]  # "SteveHislop#"
    code = separation[1]  # "16!!tv5dekdz8x11ddkc"

    numbers = code.split("!!")  # "16", "tv5dekdz8x11ddkc"

    cut = name[1:-1]
    if cut.isalpha():
        left = name[0]
        right = name[-1]
        if left == "#" or "$" or "%" or "*" or "&":
            if left == right:
                lent = len(name)
                if text[int(lent)] == "=" and numbers[0].isdigit():
                    num_len = int(len(numbers[0]))
                    cut_code = code[num_len:]
                    len_code = len(cut_code) - 2
                    if int(numbers[0]) == len_code:
                        detect = len(numbers[0])
                        cutt = code[int(detect):]
                        if cutt.startswith("!!"):
                            cuts = cutt[2:]
                            for cod in cuts:
                                ordd = ord(cod) + int(numbers[0])
                                chars = chr(ordd)
                                save.append(chars)
                            s = "".join(save)
                            print(f"Coordinates found! {cut} -> {s}")
                            break

                        else:
                            print("Nothing found!")
                            continue
                    else:
                        print("Nothing found!")
                        continue
                else:
                    print("Nothing found!")
                    continue
            else:
                print("Nothing found!")
                continue
        else:
            print("Nothing found!")
            continue
    else:
        print("Nothing found!")
        continue