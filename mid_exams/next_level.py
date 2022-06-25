# Write a program, that helps a player figure
# how many battles he will need to play in a battle video game,
# in order to unlock the next tank in the line.

target_experience = int(input())
count_battles = int(input())
total_exp = 0
target_is_reached = False
battle_count = 0

for current_battle in range(1, count_battles + 1):
    current_exp = float(input())
    total_exp += current_exp
    battle_count += 1

    if current_battle % 3 == 0:
        total_exp += current_exp*0.15
    if current_battle % 5 == 0:
        total_exp -= current_exp * 0.1
    if current_battle % 15 == 0:
        total_exp += total_exp*0.05

    if total_exp >= target_experience:
        target_is_reached = True
        break

if target_is_reached:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    needed_exp = abs(target_experience - total_exp)
    print(f"Player was not able to collect the needed experience, {needed_exp:.2f} more needed.")
