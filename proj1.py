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

    '''
    player movement = player position + movememnt direction.
    start at 2,2. move east -1, 0. move north 0, 1. move south 0, -1, move west 1, 0
    1,1; 1,2; 1,3 == east. 2,1; 2,2; 2,3 == vertical center. 3,1; 3,2; 3,3 == west.
    1,1; 2,1; 3,1 == north. 1,2; 2,2; 3,2 == horizontal center. 1,3; 2,3; 3,3 == south.
    if move direction + player position is outside range 1 , 3; theres nothing there.
    cry/action/leave - in room
    listen/go back - in hall
    '''
def hallway_text():
    '''
    hallways move includes choice to enter room at player pos + move dir
        else current position repeat
    '''
def rooms_text():
    '''
    entered room flag? to check for item/ first time text?
    play action = cry/action/leave
   1,1 bathing room 1
   1,2 storeroom 2
   1,3 library 3
   2,1 bunk room 4
   2,2 central room/start 5
   2,3 office 6
   3,1 kitchen 7
   3,2 dining room 8
   3,3 ritual room 9
    '''
def items_text():
    '''
    items defined as number assigned to room. 1-9.
    if number in inventory[] list, item not picked up
    else read idtem text.
    randomize items???
    1. Bishops scepter - bathing room
    2. dead gurl jewelry - store room
    3. bad guy item/ handcuff key - central/start
    4. ritual book - library
    5. wineskin - bunk room
    6. wax seal stamp - office
    7. campari bottle - kitchen
    8. candelabra/butcher knife/ rib or finger bone - dining room
    9. obsidian blade - ritual room
    '''
def inventory():
    '''
    function of room,
    essentially, if new room, add number to list, else read room description
    '''
def end():
    '''
    Ritual: demon consumes soul
    bad guy: bad guy consumes flesh
    cry end: knowledge consumes mind (only if all items)

    '''