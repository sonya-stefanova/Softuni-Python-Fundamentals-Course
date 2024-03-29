def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_characters = ['@', '#', '$', '^']
    for winning_ch in winning_characters:
        for repetition in range(10, 5, -1):
            character_repetition = winning_ch * repetition
            if character_repetition in left_half and character_repetition in right_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {len(character_repetition)}{winning_ch} Jackpot!'
                elif 6 <= repetition <= 9:
                    return f'ticket "{ticket}" - {len(character_repetition)}{winning_ch}'


tickets = [s.strip() for s in input().split(", ")]
tickets_state = []
for ticket in tickets:
    tickets_state.append(is_winning(ticket))
print("\n".join(ticket_state for ticket_state in tickets_state))
