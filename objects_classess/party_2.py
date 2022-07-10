class Party:
    def __init__(self):
        self.people = []  # <-- вътре добавяме имената


party = Party()  # конструираме си инстанцията

command = input()
while command != "End":
    name = command
    party.people.append(name) #<-- добави имената на хората в атрибута към инстанцията на класа
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
