class Field:

    FIELD_SIZE = 10

    def __init__(self):
        self.field = [[None] * self.FIELD_SIZE for _ in range(self.FIELD_SIZE)]

    def size(self):
        return self.FIELD_SIZE

    def set(self, n, x, y, hor, ship):
        for delta in range(n):
            if hor:
                self.field[x + delta][y] = ship
            else:
                self.field[x][y + delta] = ship

        return self.field

    def print_field(self):
        tmp_str = ''
        for i in range(-1, self.FIELD_SIZE + 1):
            if i == -1 or i == self.FIELD_SIZE:
                tmp_str = tmp_str + '+'+ '-' * self.FIELD_SIZE + '+' + '\n'
            else:
                tmp_str = tmp_str + "|"
                for point in self.field[i]:
                    tmp_str = tmp_str + (" " if point is None else str(point))
                tmp_str = tmp_str + "|\n"
        print(tmp_str)
        return None

    def free_space(self, n, x, y, hor, ship):
        if hor:
            for i in range(max(0, x - 1), self.__max_border(x, n)):
                for j in range (max(0, y - 1), self.__max_border(y, 1)):
                    if not self.__is_valid(i, j, ship):
                        return False
        else:
            for i in range(max(0, x - 1), self.__max_border(x, 1)):
                for j in range (max(0, y - 1), self.__max_border(y, n)):
                    if not self.__is_valid(i, j, ship):
                        return False
        return True

    def __is_valid(self, i, j, ship):
        if (i < 0) or (j < 0) or (i >= self.FIELD_SIZE) or (j >= self.FIELD_SIZE):
            return False
        if self.field[i][j] not in [ship, None]:
            return False
        return True

    def __max_border(self, start, n):
        return (start + n) if (start + n) == self.FIELD_SIZE else (start + n + 1)


if __name__ == "__main__":
    f = Field()
    f.set(4, 3, 3, False, 1)
    f.set(3, 5, 4, True, 2)
    f.set(1, 9, 9, True, 3)
    f.print_field()

    print(f.free_space(4, 0, 3, True, 1))
    print(f.free_space(4, 1, 3, True, 1))
    print(f.free_space(4, 7, 2, True, 1))

