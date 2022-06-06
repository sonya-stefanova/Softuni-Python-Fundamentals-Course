tail = input()
body = input()
head = input()

meerkat_body = [tail, body, head]
# meerkat_body[0], meerkat_body[2] = meerkat_body[2], meerkat_body[0]

# meerkat_body = [head, body, tail]

meerkat_body.reverse()

print(meerkat_body)