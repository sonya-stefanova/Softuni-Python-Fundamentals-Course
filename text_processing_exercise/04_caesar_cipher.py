symbols = input()
encrypted_text = []

for symbol in symbols:
    encrypted_text.append(ord(symbol)+3)
encrypted_text_chars = [chr(i) for i in encrypted_text]
print(f"{''.join(encrypted_text_chars)}")