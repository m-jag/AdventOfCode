import re

monkeyRegex = re.compile(
r"""
Monkey\ (?P<monkeyNum>\d+):\n
\ \ Starting\ items:\ (?P<startingItems>(?:\d+,\ )*\d+)\n
\ \ Operation:\ (?P<operation>[\w\d\ =+*]+)\n
\ \ Test:\ divisible\ by\ (?P<test>\d+)\n
\ \ \ \ If\ true:\ throw\ to\ monkey\ (?P<trueTarget>[\d]+)\n
\ \ \ \ If\ false:\ throw\ to\ monkey\ (?P<falseTarget>[\d]+)
""", re.VERBOSE)

class Monkey:
    def __init__(self,
                monkeyNum : str, 
                startingItems: str, 
                operation: str, 
                test: str, 
                trueTarget: str, 
                falseTarget: str):
        self.monkeyNum = int(monkeyNum)
        self.startingItems = startingItems.split(", ")
        self.operation = operation
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
    
    @staticmethod
    def createMonkeyFromBlob(blob: str):
        monkey = None
        if monkeyRegex.match(blob):
            monkeyNum = monkeyRegex.match(blob).group("monkeyNum")
            startingItems = monkeyRegex.match(blob).group("startingItems")
            operation = monkeyRegex.match(blob).group("operation")
            test = monkeyRegex.match(blob).group("test")
            trueTarget = monkeyRegex.match(blob).group("trueTarget")
            falseTarget = monkeyRegex.match(blob).group("falseTarget")
            monkey = Monkey(monkeyNum, startingItems, operation, test, trueTarget, falseTarget)
        else:
            print("Failed to Match Monkey")
        return monkey

    def __repr__(self):
        return "Monkey {:d}".format(self.monkeyNum)


with open("input.txt") as f:
    monkeys = f.read().split("\n\n")
    '''
    monkeys = monkeyRegex.findall(f.read())

    for monkey in monkeys:
        m = Monkey(*monkey)
        print(m)
    '''
    
    for monkey in monkeys:
        m = Monkey.createMonkeyFromBlob(monkey)
        print(m)