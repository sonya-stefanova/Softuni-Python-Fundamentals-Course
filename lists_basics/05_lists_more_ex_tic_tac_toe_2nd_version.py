first_line = input().split(' ')
second_line = input().split(' ')
third_line = input().split(' ')

empty_space = '0'
first_player = '1'
second_player = '2'

if first_player == first_line[0] and first_player == first_line[1] and first_player == first_line[2]:
    print('first_player player won')
elif first_player == second_line[0] and first_player == second_line[1] and first_player == second_line[2]:
    print('first_player player won')
elif first_player == third_line[0] and first_player == third_line[1] and first_player == third_line[2]:
    print('first_player player won')
elif first_player == first_line[0] and first_player == second_line[0] and first_player == third_line[0]:
    print('first_player player won')
elif first_player == first_line[1] and first_player == second_line[1] and first_player == third_line[1]:
    print('first_player player won')
elif first_player == first_line[2] and first_player == second_line[2] and first_player == third_line[2]:
    print('first_player player won')
elif first_player == first_line[0] and first_player == second_line[1] and first_player == third_line[2]:
    print('first_player player won')
elif first_player == first_line[2] and first_player == second_line[1] and first_player == third_line[0]:
    print('first_player player won')
elif second_player == first_line[0] and second_player == first_line[1] and second_player == first_line[2]:
    print('second_player player won')
elif second_player == second_line[0] and second_player == second_line[1] and second_player == second_line[2]:
    print('second_player player won')
elif second_player == third_line[0] and second_player == third_line[1] and second_player == third_line[2]:
    print('second_player player won')
elif second_player == first_line[0] and second_player == second_line[0] and second_player == third_line[0]:
    print('second_player player won')
elif second_player == first_line[1] and second_player == second_line[1] and second_player == third_line[1]:
    print('second_player player won')
elif second_player == first_line[2] and second_player == second_line[2] and second_player == third_line[2]:
    print('second_player player won')
elif second_player == first_line[0] and second_player == second_line[1] and second_player == third_line[2]:
    print('second_player player won')
elif second_player == first_line[2] and second_player == second_line[1] and second_player == third_line[0]:
    print('second_player player won')
else:
    print('Draw!')
