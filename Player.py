import random
from Field import Field


class Player:

    def reset(self):
        self.all_shots = list()
        self.last_shots = list()

    def __init__(self, name, manual=True):
        self.name = name
        self.manual = manual
        self.last_sample = [1, 0]
        self.all_shots = list()
        for i in range(0, Field.FIELD_SIZE):
            for j in range(0, Field.FIELD_SIZE):
                self.all_shots.append([i, j])
        self.shot = list()
        self.last_shots = list()

    def random_point(self):
        return [random.randint(0, Field.FIELD_SIZE - 1), random.randint(0, Field.FIELD_SIZE - 1)]

    def place_strategy(self, ship_list):
        ans = list()
        ship_list.sort(key = lambda x: x[1])
        field = Field()
        for [i, len] in ship_list:
            [x, y] = self.random_point()
            hor = random.choice([True, False])
            while not field.free_space(len, x, y, hor, i):
                [x, y] = self.random_point()
                hor = random.choice([True, False])
            field.set(len, x, y, hor, i)
            ans.append([i, x, y, hor])
        field.print_field()
        return ans

    def shooting_point(self):
        return random.choice(self.all_shots)

    def hit(self, message):
        if message.find("kill") != -1:

            self.last_shots.append([self.shot, "wounded"])

            min_x = Field.FIELD_SIZE
            max_x = -1

            min_y = Field.FIELD_SIZE
            max_y = -1

            for [shot, mes] in self.last_shots:
                if mes == "wounded":
                    min_x = min(min_x, shot[0])
                    max_x = max(max_x, shot[0])
                    min_y = min(min_y, shot[1])
                    max_y = max(max_y, shot[1])

            for i in range(min_x - 1, max_x + 2):
                for j in range(min_y - 1, max_y + 2):
                    if [i, j] in self.all_shots:
                        self.all_shots.remove([i, j])
            self.last_shots = list()
        else:
            self.last_shots.append([self.shot, message])
            self.all_shots.remove(self.shot)

    def miss(self):
        if (self.shot not in self.all_shots):
            print(self.shot)
            print(self.all_shots)
        self.all_shots.remove(self.shot)
        if len(self.last_shots) > 0:
            self.last_shots.append([self.shot, "miss"])
                #for i in range.last_shots:
               #     if shot[1].find("wounded")

        else:
            self.last_shots = list()
        #self.last_shots.append([self.shot, "miss"])
        #self.all_shots.extend(self.last_shots)
        # self.last_shots = list()

    def shot_strategy(self):
        if self.manual:
            a, b = map(int, input().split())
            return [a, b]
        else:
            if len(self.last_shots) == 0:
                self.shot = self.shooting_point()
                return self.shot
            elif self.last_shots[-1][1] == "wounded":
                if len(self.last_shots) > 1:
                    tmp = [self.shot[0] + self.last_sample[0], self.shot[1] + self.last_sample[1]]
                    if (tmp[0] < 0) | (tmp[0] >= Field.FIELD_SIZE) | (tmp[1] < 0) | (tmp[1] >= Field.FIELD_SIZE) or (tmp not in self.all_shots):
                        self.last_sample = [self.last_sample[0] * -1, self.last_sample[1] * -1]
                        self.shot = self.last_shots[0][0]

                    self.shot = [self.shot[0] + self.last_sample[0], self.shot[1] + self.last_sample[1]]
                    return self.shot

            else:
                n = 0
                for shot in self.last_shots:
                    if shot[1] == "wounded":
                        n +=1

                if n > 1:
                    self.last_sample = [self.last_sample[0] * -1, self.last_sample[1] * -1]
                    self.shot = self.last_shots[0][0]
                    self.shot = [self.shot[0] + self.last_sample[0], self.shot[1] + self.last_sample[1]]
                    return self.shot

            tmp_list = list()
            for shot in self.last_shots:
                tmp_list.append(shot[0])

            self.last_sample = self.random_dx()
            tmp = [self.last_shots[0][0][0] + self.last_sample[0], self.last_shots[0][0][1] + self.last_sample[1]]
            while ((tmp[0] < 0) | (tmp[0] >= Field.FIELD_SIZE) | (tmp[1] < 0) | (tmp[1] >= Field.FIELD_SIZE)) or (tmp not in self.all_shots):
                self.last_sample = self.random_dx()
                tmp = [self.last_shots[0][0][0] + self.last_sample[0], self.last_shots[0][0][1] + self.last_sample[1]]

            self.shot = tmp

            # tmp = list()
            # for shot in self.last_shots:
            #     tmp.append(shot[0])
            #
            # if self.shot in tmp:
            #     return self.shot_strategy()
            return self.shot

    def random_dx(self):
        hor = random.choice([True, False])
        up = random.choice([True, False])

        if hor:
            if up:
                return [1, 0]
            else:
                return [-1, 0]
        else:
            if up:
                return [0, 1]
            else:
                return [0, -1]



if __name__ == "__main__":
    player = Player("chmo")
    print(player.place_strategy([[1, 4],[2, 3],[3, 3],[4, 2],[5, 2],[6, 2],[7, 1],[8, 1],[9, 1],[0, 1]]))
