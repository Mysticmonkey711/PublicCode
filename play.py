def player_move(player_position_x, player_position_y):
    movement = input('North, South, East, or West?').title()

    potential_x = player_position_x +1
    potential_x = player_position_x -1
    potential_y = player_position_y +1
    potential_y = player_position_y -1

    print(player_position_x, player_position_y, 'in Function start')

    if movement == 'North' and potential_x < 3:
        player_position_x = player_position_x - 1
    elif movement == 'South' and potential_x > 1:
        player_position_x = player_position_x + 1
    elif movement == 'East' and potential_y < 3:
        player_position_y = player_position_y + 1
    elif movement == 'West' and potential_y > 1:
        player_position_y = player_position_y - 1
    else:
        print('There is nothing that way')

    print(player_position_x, player_position_y, 'in Function end')
    return player_position_x, player_position_y



player_position_x = 2
player_position_y = 2
print(player_position_x, player_position_y, 'In main')
i=0
while i < 6:
    player_position_x, player_position_y = player_move(player_position_x, player_position_y)
    i = i +1
    print(player_position_x, player_position_y, 'In loop')