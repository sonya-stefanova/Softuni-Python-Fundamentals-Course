command = input()
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
players_pool = {}

while command != "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players_pool.keys():
            players_pool[player] = dict()
        if position not in players_pool[player]:
            players_pool[player][position] = 0
        if skill > players_pool[player][position]:
            players_pool[player][position] = skill

    elif "vs" in command:
        player1, player2 = command.split(" vs ") #[Johny, Peter]
        winner = " "
        for player1_position in players_pool[player1].keys():
            if player1_position in players_pool[player2].keys():
                player1_skill = sum(players_pool[player1].values())
                player2_skill = sum(players_pool[player2].values())
                if player1_skill < player2_skill:
                    players_pool.pop(player1)
                elif player2_skill < player1_skill:
                    players_pool.pop(player1)
                break

    command = input()
player_points = [(key, sum(players_pool[key].values())) for key in players_pool.keys()]
player_ranking = [player for player in sorted(player_points, key= lambda x: (-x[1], x[0]))]

for rank in player_ranking:
    player, skill = rank
    print(f"{player}: {skill} skill")
    position_ranking = [rank for rank in sorted(players_pool[player].items(), key= lambda x: (-x[1], x[0]))]
    output = [f'- {pos} <::> {skill}' for pos, skill in position_ranking]
    print(*output, sep='\n')
