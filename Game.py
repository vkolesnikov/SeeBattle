from Player import Player
from BattleField import BattleField


class Game:

    def __init__(self, player_1, player_2):
        self.players = [[player_1, BattleField(), 0], [player_2, BattleField(), 0]]
        for p in self.players:
            self.reset(p)
        self.game_over = False

    def reset(self, p):
        [player, bfield, _] = p
        print(player.name + " game setup")
        ships = bfield.fleet()
        plan = player.place_strategy(ships)
        if bfield.place_fleet(plan):
            print("Ships placed")
        else:
            raise Exception("Illegal ship placement")

    def start(self):
        last_shots = list()
        active = 0
        while True:
            passive = (active + 1) % 2
            self.players[active][2] += 1
            print("Step " + str(self.players[active][2]) + " of player " + str(self.players[active][0].name))
            remains = self.players[active][1].remains()
            shot = self.players[active][0].shot_strategy()
            res = ""
            if shot in last_shots:
                print("Illegal shot")
                res = "miss"
            else:
                res = self.players[passive][1].shoot(shot)
            last_shots.append(shot)
            print(str(shot) + " " + res)
            if res == "miss":
                self.players[active][0].miss()
                last_shots = list()
                self.print_st(active)
                active = passive
            else:
                self.players[active][0].hit(res)
                self.game_over = self.players[passive][1].is_game_over()
                self.print_st(active)

            if self.game_over:
                print("Player " + self.players[active][0].name + " wins!")
                break

    def print_st(self, active):
        tmp_str = ''
        passive = (active + 1) % 2
        for i in range(-1, 10 + 1):
            if i == -1 or i == 10:
                tmp_str = tmp_str + '+' + '-' * 10 + '+' + '\n'
            else:
                tmp_str = tmp_str + "|"
                for j in range(0, 10):
                    point = self.players[passive][1].field[i][j]
                    tmp = (" " if point is None else str(point))

                    if [i, j] not in self.players[active][0].all_shots:
                        if tmp == " ":
                            tmp = "*"
                        else:
                            tmp = '!'
                    tmp_str = tmp_str + tmp
                tmp_str = tmp_str + "|\n"
        print(tmp_str)

if __name__ == "__main__":
    p1 = Player("Ivan", False)
    p2 = Player("Feodor", False)
    g = Game(p1, p2)
    g.start()




