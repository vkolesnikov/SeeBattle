from Field import Field
from Ship import Ship


class BattleField(Field):

    SHIPS = [4,3,3,2,2,2,1,1,1,1]

    def new_ships(self):
        for length in self.SHIPS:
            self.all_ships.append(Ship(self, length))

    def __init__(self):
        super().__init__()
        self.all_ships = list()
        self.new_ships()

    def fleet(self):
        ans = list()
        for i in range(len(self.SHIPS)):
            ans.append([i, self.SHIPS[i]])
        return ans

    def place_fleet(self, pos_list):
        for [i, x, y, hor] in pos_list:
            if not self.all_ships[i].set(x, y, hor):
                for ship in self.all_ships:
                    ship.clear()
                return False
        return True

    def remains(self):
        ans = list()
        for i in range(len(self.all_ships)):
            ans.append([i, self.all_ships[i].coord, self.all_ships[i].len, self.all_ships[i].health])
            '''/ self.all_ships[i].max_health * 100]'''
        return ans

    def refresh(self):
        tmp = list()
        for ship in self.all_ships:
            if ship.health != 0:
                tmp.append(ship)
        self.all_ships = tmp

    def shoot(self, c):
        [x, y] = c

        if (x < 0) or (x >= self.FIELD_SIZE) or (y < 0) or (y >= self.FIELD_SIZE):
            return "miss"

        if self.field[x][y] is None:
            return "miss"
        else:
            # ans = self.field[x][y].explode()
            # if ans is None:
            #     return "wounded"
            # else:
            #     return "killed " + str(ans)
            return self.field[x][y].explode()

    def is_game_over(self):
        self.refresh()
        return True if len(self.all_ships) == 0 else False

