class Ship:

    def __init__(self, field, len):
        self.len = len
        self.my_field = field
        self.max_health = len
        self.min_health = 0
        self.health = len
        self.coord = None
        self.hor = None

    def len(self):
        return self.len

    def coord(self):
        return None

    def __str__(self):
        return "X"

    def clear(self):
        if self.my_field.free_space(self.len, self.coord[0][0], self.coord[0][1], self.hor, self):
            self.my_field.set(self.len, self.coord[0][0], self.coord[0][1], self.hor, None)

    def set(self, x, y, hor):
        if self.my_field.free_space(self.len, x, y, hor, self):
            if self.coord is not None:
                self.clear()
            self.hor = hor
            self.coord = [[x, y], [x + self.len, y]] if not hor else [[x, y], [x, y + self.len]]
            self.my_field.set(self.len, self.coord[0][0], self.coord[0][1], self.hor, self)
            return True
        return False

    def kill(self):
        self.clear()
        self.coord = None

    def explode(self):
        if self.health == 0:
            return "miss"
        self.health -= 1
        if self.health <= self.min_health:
            #self.kill()
            return "kill " + str(self.len)
        #return None
        return "wounded"
