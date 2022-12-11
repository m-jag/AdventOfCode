import re
import math

monkeyRegex = re.compile(
r"""
Monkey\ (?P<monkeyNum>\d+):\n
\ \ Starting\ items:\ (?P<startingItems>(?:\d+,\ )*\d+)\n
\ \ Operation:\ (?P<operation>[\w\d\ =+*]+)\n
\ \ Test:\ divisible\ by\ (?P<divisor>\d+)\n
\ \ \ \ If\ true:\ throw\ to\ monkey\ (?P<trueTarget>[\d]+)\n
\ \ \ \ If\ false:\ throw\ to\ monkey\ (?P<falseTarget>[\d]+)
""", re.VERBOSE)

class Monkey:
    def __init__(self,
                monkeyNum : str, 
                startingItems: str, 
                operation: str, 
                divisor: str, 
                trueTarget: str, 
                falseTarget: str):
        self.monkeyNum = int(monkeyNum)
        self.items = list(int(x) for x in startingItems.split(", "))
        self.operation = operation
        self.divisor = int(divisor)
        self.trueTarget = int(trueTarget)
        self.falseTarget = int(falseTarget)
        self.numInspections = 0
        
        self.OperationRegex = re.compile(r"new = old (?P<op>[\*\+]) (?P<param>[\w\d]+)")
        self.NumberRegex = re.compile("(?P<number>-?\d+)")
        self.OldRegex = re.compile("old")
        self.cm = None
    

    def runOperation(self):
        # Get Item
        currentItem = self.items.pop(0)
        self.numInspections += 1

        # Apply Operation
        if self.OperationRegex.match(self.operation):
            op = self.OperationRegex.match(self.operation).group("op")
            param = self.OperationRegex.match(self.operation).group("param")
            if self.NumberRegex.match(param):
                param = int(self.NumberRegex.match(param).group("number"))
            elif self.OldRegex.match(param):
                param = currentItem
            else:
                raise Exception(f"Operation: Unexpected Param {param}")
            
            if op == "+":
                currentItem += param
            elif op == "*":
                currentItem *= param
            else:
                raise Exception("Operation: Unexpected Operation")
        
        # Apply LCM Rule
        if self.cm is not None:
            currentItem = currentItem % self.cm

        return currentItem
    
    @staticmethod
    def createMonkeyFromBlob(blob: str):
        monkey = None
        if monkeyRegex.match(blob):
            monkeyNum = monkeyRegex.match(blob).group("monkeyNum")
            startingItems = monkeyRegex.match(blob).group("startingItems")
            operation = monkeyRegex.match(blob).group("operation")
            divisor = monkeyRegex.match(blob).group("divisor")
            trueTarget = monkeyRegex.match(blob).group("trueTarget")
            falseTarget = monkeyRegex.match(blob).group("falseTarget")
            monkey = Monkey(monkeyNum, startingItems, operation, divisor, trueTarget, falseTarget)
        else:
            print("Failed to Match Monkey")
        return monkey

    def __repr__(self):
        itemlistStr = ", ".join(str(x) for x in self.items)
        return  f"Monkey {self.monkeyNum}: {itemlistStr}"\

ROUND_COUNT = 10000
interestingRounds = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
with open("input.txt") as f:
    monkeys = monkeyRegex.findall(f.read())
    monkeyList = []
    
    for monkey in monkeys:
        m = Monkey(*monkey)
        monkeyList.append(m)
    
    # Print Initial Status
    print(f"### Initial ###")
    for m in monkeyList:
        print(m)
    
    # Calculate Common Multiple, e.g. a small number we can consistently mod by since we don't care about the actual anxiety levels
    cm = 1
    for monkey in monkeyList:
        cm *= monkey.divisor

    # Set CM
    for monkey in monkeyList:
        monkey.cm = cm

    # Run Rounds
    for round in range(ROUND_COUNT):
        for monkey in monkeyList:
            while monkey.items:
                item = monkey.runOperation()
                if item % monkey.divisor == 0:
                    monkeyList[monkey.trueTarget].items.append(item)
                else:
                    monkeyList[monkey.falseTarget].items.append(item)

        # Print Status After Round
        if (round + 1) in interestingRounds:
            print(f"== After round {round + 1} ==")
            for m in monkeyList:
                print(f"Monkey {m.monkeyNum} inspected items {m.numInspections} times.")
    
    # Dump Inspection Count
    MAX_TOP_INSPECT_CNTS = 2
    topInspectionCounts = []
    for m in monkeyList:
        print(f"Monkey {m.monkeyNum} inspected items {m.numInspections} times.")
        topInspectionCounts.append(m.numInspections)
        if len(topInspectionCounts) > MAX_TOP_INSPECT_CNTS:
            topInspectionCounts.remove(min(topInspectionCounts))
    
    # Determine Level of Monkey Business
    levelOfMonkeyBusiness = topInspectionCounts[0] * topInspectionCounts[1]
    print(f"Level of Monkey Business: {levelOfMonkeyBusiness}")

        
