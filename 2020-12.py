import sys
import math
from enum import Enum

class Dir(Enum):
    N=0
    E=1
    S=2
    W=3

    def right(self, turns=1):
        return Dir((self.value+turns) % 4)

    def left(self, turns=1):
        return Dir((self.value+4-turns) % 4)

    def wpright(self, turns=1):
        return Dir((self.value+turns) % 4)

    def wpleft(self, turns=1):
        return Dir((self.value+4-turns) % 4)

class Ship:
    x = 0
    y = 0
    dir = Dir.E

    def N(self, dist):
        self.y += dist

    def E(self, dist):
        self.x += dist

    def S(self, dist):
        self.y -= dist

    def W(self, dist):
        self.x -= dist

    def F(self, dist):
        self.op(self.dir.name, dist)

    def R(self, degrees):
        self.dir = self.dir.right(int(degrees / 90))

    def L(self, degrees):
        self.dir = self.dir.left(int(degrees / 90))

    def op(self, code, arg):
        getattr(self, code)(arg)


class Waypoint:
    x = 10
    y = 1

    def N(self, dist):
        self.y += dist

    def E(self, dist):
        self.x += dist

    def S(self, dist):
        self.y -= dist

    def W(self, dist):
        self.x -= dist

    def R(self, ship, degrees):
        self.rotate(ship, -math.radians(degrees))

    def L(self, ship, degrees):
        self.rotate(ship, math.radians(degrees))

    def rotate(self, ship, radians):
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = ship.x + round((self.x - ship.x)*cos - (self.y - ship.y)*sin)
        y = ship.y + round((self.x - ship.x)*sin + (self.y - ship.y)*cos)
        [self.x, self.y] = [x, y]


class Ship2:
    x = 0
    y = 0
    waypoint = Waypoint()

    def N(self, dist):
        self.waypoint.N(dist)

    def E(self, dist):
        self.waypoint.E(dist)

    def S(self, dist):
        self.waypoint.S(dist)

    def W(self, dist):
        self.waypoint.W(dist)

    def R(self, degrees):
        self.waypoint.R(self, degrees)

    def L(self, degrees):
        self.waypoint.L(self, degrees)

    def F(self, dist):
        dx = self.waypoint.x - self.x
        dy = self.waypoint.y - self.y
        self.x += dx * dist
        self.y += dy * dist
        self.waypoint.x += dx * dist
        self.waypoint.y += dy * dist

    def op(self, code, arg):
        getattr(self, code)(arg)

ship = Ship()
ship2 = Ship2()

for line in sys.stdin:
    op = line[0]
    arg = int(line[1:])
    ship.op(op, arg)
    ship2.op(op, arg)
    # print(f'{line.strip()}: {ship.x},{ship.y} {ship.dir}')
    # print(f'{line.strip()}: {ship2.x},{ship2.y} {ship2.waypoint.x},{ship2.waypoint.y}')

# part 1: 1589
print(abs(ship.x) + abs(ship.y))

# part 2: 23960
print(abs(ship2.x) + abs(ship2.y))
