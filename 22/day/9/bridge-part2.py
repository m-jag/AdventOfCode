import re
from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

NUM_KNOTS = 10
class RopeSimulator:
    def __init__(self):
        self.max = Point(0, 0)
        self.min = Point(0, 0)
        self.knots = []
        for _ in range(NUM_KNOTS):
            self.knots.append(Point(0, 0))
        self.startingPos = Point(0, 0)
        self.motionRegex = re.compile(r"(?P<direction>\w) (?P<distance>[\d]+)")
        self.positionsVisited = []
    def parseMotion(self, motion: str):
        if self.motionRegex.match(motion):
            direction = self.motionRegex.match(motion).group("direction")
            distance = int(self.motionRegex.match(motion).group("distance"))
            print("Direction: {direction:s}, Distance: {distance:d}".format(direction = direction, distance = distance))
            
            for _ in range(distance):
                if direction == "U":
                    self.knots[0].y += 1
                elif direction == "D":
                    self.knots[0].y -= 1
                elif direction == "L":
                    self.knots[0].x -= 1
                elif direction == "R":
                    self.knots[0].x += 1
                for i in range(1, NUM_KNOTS):
                    if abs(self.knots[i - 1].x - self.knots[i].x) >= 2:
                        self.knots[i].x += int((self.knots[i - 1].x - self.knots[i].x) / abs(self.knots[i - 1].x - self.knots[i].x))
                        if self.knots[i - 1].y != self.knots[i].y:
                            self.knots[i].y += int((self.knots[i - 1].y - self.knots[i].y) / abs(self.knots[i - 1].y - self.knots[i].y))
                    elif abs(self.knots[i - 1].y - self.knots[i].y) >= 2:
                        self.knots[i].y += int((self.knots[i - 1].y - self.knots[i].y) / abs(self.knots[i - 1].y - self.knots[i].y))
                        if self.knots[i - 1].x != self.knots[i].x:
                            self.knots[i].x += int((self.knots[i - 1].x - self.knots[i].x) / abs(self.knots[i - 1].x - self.knots[i].x))
                if self.knots[0].x + 1 > self.max.x:
                    self.max.x = self.knots[0].x + 1
                if self.knots[0].y + 1 > self.max.y:
                    self.max.y = self.knots[0].y + 1
                if self.knots[0].x < self.min.x:
                    self.min.x = self.knots[0].x
                if self.knots[0].y < self.min.y:
                    self.min.y = self.knots[0].y
                if not self.knots[9] in self.positionsVisited:
                    self.positionsVisited.append(deepcopy(self.knots[9]))
                '''
                for i in range(1, NUM_KNOTS):
                    if not self.knots[i] in self.positionsVisited:
                        self.positionsVisited.append(deepcopy(self.knots[i]))
                '''
                #self.showSimulationState()
        else:
            print("\033[91mUnexpected Motion: \"{motion:s}\"\033[0m".format(motion = motion))
    def showSimulationState(self):
        diagram = []
        for row in range(abs(self.min.y) + self.max.y + 1):
            diagram.append([])
            for _ in range(abs(self.min.x) + self.max.x + 1):
                diagram[row].append(".")
        print("Head: ({}, {})".format(self.knots[0].x, self.knots[0].y))
        print("Tail: ({}, {})".format(self.knots[0].x, self.knots[0].y))
        
        diagram[abs(self.min.y) + self.startingPos.y][abs(self.min.x) + self.startingPos.x] = "s"
        for i in range(NUM_KNOTS - 1, 0, -1):
            diagram[abs(self.min.y) + self.knots[i].y][abs(self.min.x) + self.knots[i].x] = str(i)
        diagram[abs(self.min.y) + self.knots[0].y][abs(self.min.x) + self.knots[0].x] = "H"
        print("\n".join("".join(line) for line in diagram[::-1]))

    def showPlacesVisited(self):
        diagram = []
        for row in range(abs(self.min.y) + self.max.y + 1):
            diagram.append([])
            for _ in range(abs(self.min.x) + self.max.x + 1):
                diagram[row].append(".")
        
        for place in self.positionsVisited:
            diagram[abs(self.min.y) + place.y][abs(self.min.x) + place.x] = "#"
        diagram[abs(self.min.y) + self.startingPos.y][abs(self.min.x) + self.startingPos.x] = "s"

        print("Places Visited:")
        print("\n".join("".join(line) for line in diagram[::-1]))

with open("input.txt") as f:
    motions = f.read().split("\n")

    sim = RopeSimulator()
    #sim.showSimulationState()
    for motion in motions:
        sim.parseMotion(motion)
    sim.showPlacesVisited()
    print("Positions Visited: {:d}".format(len(sim.positionsVisited)))