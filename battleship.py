ORIENTATION_DICT = {'N': 1,
                    'E': 2,
                    'S': 3,
                    'W': 4}
INVERT_ORIENTATION_DICT = {v: k for k, v in ORIENTATION_DICT.items()}


class Battleship:
    """ Battleship class is a NxN matrix which represents ships positions.
    Each cell contains an integer which represents ship's orientation."""

    def __init__(self, board_size):
        """Create an empty board"""
        try:
            self.board_size = int(board_size)
            self.board = [[0 for _ in range(self.board_size)]
                          for _ in range(self.board_size)]
            self.sunken_ships = []
        except ValueError:
            print("Board's size should be an integer")

    def place_ship(self, x_index, y_index, orientation):
        """Place a ship on given coordinates if it's not occupied by another ship"""
        try:

            if int(x_index) < 0 or int(y_index) < 0:
                raise IndexError
            if orientation not in ORIENTATION_DICT.keys():
                raise Exception("Ship orientation should be one of 'N', 'S', 'W', 'E'")
            if self.board[int(x_index)][int(y_index)]:
                raise Exception('Ship already exists at this location')

            self.board[int(x_index)][int(y_index)] = ORIENTATION_DICT[orientation]
            return True

        except ValueError:
            print("Ships coordinates should be an integer")
            return False
        except IndexError:
            print("Ships coordinates should be in range 0.."+str(self.board_size-1))
            return False
        except Exception as Err:
            print(Err)
            return False

    def move_ship(self, x, y, operations):
        """ Move existing ship to a new location\change it's orientation"""
        try:
            if int(x) < 0 or int(y) < 0:
                raise IndexError
            ship_or = self.board[int(x)][int(y)]
            if ship_or == 0:
                raise Exception("No ship in given position "+x+","+y)
            curr_x = int(x)
            curr_y = int(y)
            location_changed = False
            for op in operations:
                if op == 'M':
                    if ship_or == ORIENTATION_DICT['N']:
                        curr_y = curr_y + 1
                    elif ship_or == ORIENTATION_DICT['E']:
                        curr_x = curr_x + 1
                    elif ship_or == ORIENTATION_DICT['S']:
                        curr_y = curr_y - 1
                    else:
                        curr_x = curr_x - 1

                    if curr_x < 0 or curr_y < 0 or curr_x > self.board_size - 1 or curr_y > self.board_size - 1:
                        raise Exception("Invalid move coordinates")
                    location_changed = True

                elif op == 'L':
                    ship_or = ship_or - 1 if ship_or > ORIENTATION_DICT['N'] else ORIENTATION_DICT['W']
                elif op == 'R':
                    ship_or = ship_or + 1 if ship_or < ORIENTATION_DICT['W'] else ORIENTATION_DICT['N']
                else:
                    raise Exception("Invalid operation")

            if location_changed:
                # place the ship at a new location
                if self.place_ship(curr_x, curr_y, INVERT_ORIENTATION_DICT[ship_or]):
                    # remove ship from it's previous position if new location is not occupied by another ship
                    self.board[int(x)][int(y)] = 0
            else:  # only ship orientation has been changed
                self.board[int(x)][int(y)] = ship_or

        except IndexError:
            print("Ships coordinates should be in range 0.."+str(len(self.board)-1))
        except Exception as Err:
            print(Err)

    def sunk_ship(self, x, y):
        """ Sunk a ship at a given location if it exists there"""
        try:
            if int(x) < 0 or int(y) < 0:
                raise IndexError

            if self.board[int(x)][int(y)]:
                # store the last position of sunken ship
                self.sunken_ships.append("({0}, {1}, {2})".format(
                    x, y, INVERT_ORIENTATION_DICT[self.board[int(x)][int(y)]]))
                self.board[int(x)][int(y)] = 0  # mark a cell as available
        except IndexError:
            print("Ships coordinates should be in range 0.."+str(len(self.board)-1))

    def __str__(self):
        """ Return a string with all information about board's ships"""
        output = ""
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] > 0:
                    output = output + "({0}, {1}, {2})\n".format(x, y, INVERT_ORIENTATION_DICT[self.board[x][y]])

        # print a list of sunken ships
        for ship in self.sunken_ships:
            output = output + ship+" SUNK\n"

        return output


