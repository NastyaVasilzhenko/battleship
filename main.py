from battleship import Battleship

X_INDEX = 1
Y_INDEX = 4
ORIENTATION_INDEX = 7
SUNK_LINE_LEN = 7


def play_battleship(input_path, output_path):

    with open(input_path, 'r') as f:
        # Create a new board
        battleship = Battleship(f.readline())
        # add ships to the board
        ships = f.readline().rstrip().split(') ')
        for ship in ships:
            battleship.place_ship(ship[X_INDEX], ship[Y_INDEX], ship[ORIENTATION_INDEX])

        # operate ships
        for line in f:
            x = line[X_INDEX]
            y = line[Y_INDEX]
            if len(line) > SUNK_LINE_LEN:  # move the ship
                operations = line[SUNK_LINE_LEN:].rstrip()
                battleship.move_ship(x, y, operations)
            else:
                battleship.sunk_ship(x, y)

    # print result to a output file
    with open(output_path, 'w') as f:
        f.write(str(battleship))
