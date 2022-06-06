team_a = []
team_b = []
is_game_terminated = False

cards = input().split()

for player_number in range(1, 12):
    team_a.append(f'A-{player_number}')
    team_b.append(f'B-{player_number}')


for player in cards:

    if player in team_a:
        team_a.remove(player)

    if player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        is_game_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if is_game_terminated:
    print('Game was terminated')
