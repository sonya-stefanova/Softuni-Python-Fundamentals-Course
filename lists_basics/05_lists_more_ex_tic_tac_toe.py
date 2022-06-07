'Tic tac toe'

first_row = input().split()
second_row = input().split()
third_row = input().split()

first_player_winning = (
              (first_row[0] == second_row[0] == third_row[0]) and first_row[0] == '1' or
              (first_row[1] == second_row[1] == third_row[1]) and first_row[1] == '1' or
              (first_row[2] == second_row[2] == third_row[2]) and first_row[2] == '1' or
              (first_row[0] == first_row[1] == first_row[2]) and first_row[0] == '1' or
              (second_row[0] == second_row[1] == second_row[2]) and second_row[0] == '1' or
              (third_row[0] == third_row[1] == third_row[2]) and third_row[0] == '1' or
              (first_row[0] == second_row[1] == third_row[2]) and first_row[0] == '1' or
              (first_row[2] == second_row[1] == third_row[0]) and first_row[2] == '1'
)

second_player_winning = (
            (first_row[0] == second_row[0] == third_row[0]) and first_row[0] == '2' or
              (first_row[1] == second_row[1] == third_row[1]) and first_row[1] == '2' or
              (first_row[2] == second_row[2] == third_row[2]) and first_row[2] == '2' or
              (first_row[0] == first_row[1] == first_row[2]) and first_row[0] == '2' or
              (second_row[0] == second_row[1] == second_row[2]) and second_row[0] == '2' or
              (third_row[0] == third_row[1] == third_row[2]) and third_row[0] == '2' or
              (first_row[0] == second_row[1] == third_row[2]) and first_row[0] == '2' or
              (first_row[2] == second_row[1] == third_row[0]) and first_row[2] == '2')

if first_player_winning:
    print("First player won")
elif second_player_winning:
    print('Second player won')
else:
    print('Draw!')