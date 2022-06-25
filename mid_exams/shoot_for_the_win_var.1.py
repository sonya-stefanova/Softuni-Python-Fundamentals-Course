shot_targets = [int(target) for target in input().split()]
command = input()
while command != 'End':
    idx = int(command)

    if idx in range(len(shot_targets)):
        current_target = shot_targets[idx]
        shot_targets[idx] = -1

        for target in range(len(shot_targets)):
            if shot_targets[target] != -1:
                if shot_targets[target] > current_target:
                    shot_targets[target] -= current_target
                else:
                    shot_targets[target] += current_target

    command = input()

print(f"Shot targets: {shot_targets.count(-1)} -> {' '.join(str(target) for target in shot_targets)}")