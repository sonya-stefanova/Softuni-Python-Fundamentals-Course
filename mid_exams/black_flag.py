target_plunder_reached = False

days = int(input())
daily_plunder = int(input())
target_plunder = float(input())
total_plunder = 0
for current_pirating_day in range(1, days+1):
    total_plunder+=daily_plunder

    if current_pirating_day % 3 == 0:
        total_plunder+=0.5*daily_plunder
    if current_pirating_day %5 == 0:
        total_plunder*=0.7

if total_plunder >= target_plunder:
    target_plunder_reached = True
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent_of_plunder = total_plunder / target_plunder * 100
    print(f"Collected only {percent_of_plunder:.2f}% of the plunder.")