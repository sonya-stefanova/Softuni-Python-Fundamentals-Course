chars = input().upper()
new_chars = ""

while len(chars) > 0:
    collect_ch = ""
    collect_num_as_str = ""

    for ch in range(len(chars)):
        if not chars[ch].isdigit():
            collect_ch += chars[ch]
        elif chars[ch].isdigit():
            collect_num_as_str += chars[ch]
            if ch + 1 < len(chars):
                if not chars[ch + 1].isdigit():
                    break

    multiplier = int(collect_num_as_str)
    new_chars += collect_ch * multiplier
    chars = chars[(len(collect_ch) + len(collect_num_as_str)):]

unique_symbols = len(set(new_chars))

print(f"Unique symbols used: {unique_symbols}")
print(new_chars)