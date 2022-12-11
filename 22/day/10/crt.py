from abc import ABC, abstractmethod
import re

SUM = 0

def isInterestingCycle(cycle: int):
    return (cycle - 20) % 40 == 0

class Instruction(ABC):
    def __init__(self, instruction, cycles):
        self.instruction = instruction
        self.cycles = cycles
    
    @abstractmethod
    def execute(self, CPU):
        pass
    
    def cycle(self):
        self.cycles -= 1
    
    def shouldExecute(self):
        return self.cycles == 0
    
    def __str__(self) -> str:
        return self.instruction
    
    def __repr__(self) -> str:
        return self.instruction

NoopInstRegex = re.compile(r"noop")
class Noop(Instruction):
    def __init__(self, instruction, cycles = 1):
        super().__init__(instruction, cycles)
    def execute(self, CPU):
        pass

AddXInstRegex = re.compile(r"addx (?P<value>-?[\d]+)")
class AddX(Instruction):
    def __init__(self, instruction, cycles = 2):
        super().__init__(instruction, cycles)
        self.value = int(AddXInstRegex.match(instruction).group("value"))
    def execute(self, CPU):
        CPU.registers["X"].add(self.value)

class Register:
    def __init__(self, initial_value = 1):
        self.value = initial_value
    def add(self, value):
        self.value += value

class CPU:
    def __init__(self):
        self.registers = {
            "X": Register()
        }
        self.instruction_queue = []
        self.cycleCount = 0

    def cycle(self):
        global SUM
        self.cycleCount += 1
        currentInstruction = self.instruction_queue[0]
        currentInstruction.cycle()
        if isInterestingCycle(self.cycleCount):
            print("Cycle {:d}: Instruction {:s} Signal Strength: {:d}".format(self.cycleCount, str(currentInstruction), self.getSignalStrength()))
            SUM += self.getSignalStrength()
        if currentInstruction.shouldExecute():
            #print("Cycle {:d}: Execute {:s} Signal Strength: {:d}".format(self.cycleCount, str(currentInstruction), self.getSignalStrength()))
            currentInstruction.execute(self)
            self.instruction_queue.pop(0)
        #else:
            #print("Cycle {:d}: Wait {:s} Signal Strength: {:d}".format(self.cycleCount, str(currentInstruction), self.getSignalStrength()))
    
    def isDone(self):
        return len(self.instruction_queue) == 0

    def processInstruction(self, instruction):
        if NoopInstRegex.match(instruction):
            self.instruction_queue.append(Noop(instruction))
        if AddXInstRegex.match(instruction):
            self.instruction_queue.append(AddX(instruction))
    
    def getSignalStrength(self):
        return self.cycleCount * self.registers["X"].value

with open("input.txt") as f:
    instructions = f.read().split("\n")

    cpu = CPU()

    for instruction in instructions:
        cpu.processInstruction(instruction)
    
    while not cpu.isDone():
        cpu.cycle()

    print("Sum of Interesting Signals: {:d}".format(SUM))