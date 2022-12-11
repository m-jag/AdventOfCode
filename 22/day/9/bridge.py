import re
from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class RopeSimulator:
    def __init__(self, width = 1, height = 1):
        self.max = Point(0, 0)
        self.min = Point(0, 0)
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
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
                    self.head.y += 1
                elif direction == "D":
                    self.head.y -= 1
                elif direction == "L":
                    self.head.x -= 1
                elif direction == "R":
                    self.head.x += 1
                if abs(self.head.x - self.tail.x) >= 2:
                    self.tail.x += int((self.head.x - self.tail.x) / abs(self.head.x - self.tail.x))
                    self.tail.y = self.head.y # this line is technically wrong
                elif abs(self.head.y - self.tail.y) >= 2:
                    self.tail.y += int((self.head.y - self.tail.y) / abs(self.head.y - self.tail.y))
                    self.tail.x = self.head.x # this line is technically wrong
                if self.head.x + 1 > self.max.x:
                    self.max.x = self.head.x + 1
                if self.head.y + 1 > self.max.y:
                    self.max.y = self.head.y + 1
                if self.head.x < self.min.x:
                    self.min.x = self.head.x
                if self.head.y < self.min.y:
                    self.min.y = self.head.y
                if not self.tail in self.positionsVisited:
                    self.positionsVisited.append(deepcopy(self.tail))
                #self.showSimulationState()
        else:
            print("\033[91mUnexpected Motion: \"{motion:s}\"\033[0m".format(motion = motion))
    def showSimulationState(self):
        diagram = []
        for row in range(abs(self.min.y) + self.max.y + 1):
            diagram.append([])
            for _ in range(abs(self.min.x) + self.max.x + 1):
                diagram[row].append(".")
        print("Head: ({}, {})".format(self.head.x, self.head.y))
        print("Tail: ({}, {})".format(self.head.x, self.head.y))
        
        diagram[abs(self.min.y) + self.startingPos.y][abs(self.min.x) + self.startingPos.x] = "s"
        diagram[abs(self.min.y) + self.tail.y][abs(self.min.x) + self.tail.x] = "T"
        diagram[abs(self.min.y) + self.head.y][abs(self.min.x) + self.head.x] = "H"
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