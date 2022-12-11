import re
from enum import Enum

def getParentPath(path: str):
    normalize(path)
    path = path.split("/")
    parentPath = "/"
    if (len(path) > 2):
        parentPath = "/".join(path[:-1])
    return parentPath
    
def normalize(path: str):
    path = path.split("/")
    index = 1
    while index < len(path):
        if index == 1 and (path[index] == ".." or path[index] == "." ):
            path.pop(index)
        elif path[index] == "..":
            path.pop(index - 1)
            path.pop(index - 1)
        elif path[index] == ".":
            path.pop(index)
        elif path[index] == "":
            path.pop(index)
        else:
            index += 1
    while len(path) <= 1:
        path.insert(0, '')
    return "/".join(path)

class File:
    def __init__(self, name : str, size : int):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name : str, parent : str):
        self.name = name
        self.parent = parent
        self.folders = []
        self.files = []
        self.directorySize = 0
    def addFile(self, filename: str, size: int):
        self.files.append(File(filename, size))
    def addFolder(self, foldername):
        self.folders.append(Directory(foldername, self.name))
    def getFile(self, path):
        path = normalize(path)
        path = path.split("/")
        try:
            folder = self.getFolder("/".join(path[:-1]))
        except:
            raise Exception("Folder Not Found")
        filename = path[-1]
        try:
            index = folder.files.index(filename)
        except:
            raise Exception("File Not Found")
        return folder.files[index]
    def getFolder(self, path):
        path = normalize(path)
        path = path.split("/")
        currFolder = self
        if len(path) == 2 and path[1] == "":
            currFolder = self
        elif len(path) >= 2:
            for part in path[1:]:
                found = False
                for folder in currFolder.folders:
                    if folder.name == part:
                        currFolder = folder
                        found = True
                        break
                if not found:
                    raise Exception("Folder Not Found")
        else:
            print("\033[91mUnexpected path: {:s}\033[0m".format("/".join(path)))
        return currFolder
    def calcDirectorySize(self):
        self.directorySize = 0
        for folder in self.folders:
            folder.calcDirectorySize()
            self.directorySize += folder.directorySize
        for file in self.files:
            self.directorySize += file.size
    def dumpFileSystem(self, tabs=0):
        print("{:s}- {:s} (dir, {:d})".format("\t"*tabs, self.name, self.directorySize))
        for folder in self.folders:
            folder.dumpFileSystem(tabs + 1)
        for file in self.files:
            print("{:s}- {:s} (file, {:d})".format("\t"*(tabs + 1), file.name, file.size))
    def dumpDirs(self, maxSize = -1):
        if (maxSize == -1):
            print("- {:s} (dir, {:d})".format(self.name, self.directorySize))
        elif (self.directorySize <= maxSize):
            print("- {:s} (dir, {:d})".format(self.name, self.directorySize))
        for folder in self.folders:
            folder.dumpDirs(maxSize)
        return self.directorySize
    def closestButBigger(self, size: int):
        closest = self.directorySize
        for folder in self.folders:
            folderSize = folder.closestButBigger(size)
            if folderSize > size:
                closest = min(closest, folderSize)
        return closest


class State(Enum):
    COMMAND = 1
    OUTPUT = 2

with open("input.txt") as f:
    stdin = f.read().split("\n")
    state = State.COMMAND
    root = Directory("/", None)

    commandRegex = re.compile(r"\$ (?P<command>[\w]+)")
    cdRegex = re.compile(r"\$ cd (?P<path>[\w/\.]+)")
    directoryRegex = re.compile(r"dir (?P<dirName>[\w/]+)")
    fileRegex = re.compile(r"(?P<fileSize>[\d]+) (?P<fileName>[\w\.]+)")

    cwd = root.name
    output_folder = ""
    for current_line in stdin:
        if  commandRegex.match(current_line):
            state == State.COMMAND
            command = commandRegex.match(current_line).group("command")
            if command == "cd":
                path = cdRegex.match(current_line).group("path")
                print("CD: {:s}".format(path))
                cwd += "/" + path
                cwd = normalize(cwd)
                try:
                    # Folder Exists
                    root.getFolder(cwd)
                except:
                    # Folder Doesn't Exist
                    parentFolder = root.getFolder(getParentPath(cwd))
                    parentFolder.addFolder(path)
            elif command == "ls":
                print("LS")
                state = State.OUTPUT
            else:
                print("\033[91mUNKNOWN COMMAND: \"{:s}\"\033[0m".format(current_line, command))
        elif state == State.OUTPUT and directoryRegex.match(current_line):
            dirName = directoryRegex.match(current_line).group("dirName")
            print("DIRECTORY: {:s}".format(dirName))
            output_folder = cwd + "/" + dirName
            output_folder = normalize(output_folder)
            try:
                # Folder Exists
                folder = root.getFolder(output_folder)
            except:
                # Folder Doesn't Exist
                parentFolder = root.getFolder(getParentPath(output_folder))
                parentFolder.addFolder(dirName)
        elif state == State.OUTPUT and fileRegex.match(current_line):
            fileSize = int(fileRegex.match(current_line).group("fileSize"))
            fileName = fileRegex.match(current_line).group("fileName")
            print("FILE: {:s} SIZE: {:d}".format(fileName, fileSize))
            try:
                # Folder Exists
                folder = root.getFolder(cwd)
                folder.addFile(fileName, fileSize)
            except:
                # Folder Doesn't Exist
                print("\033[91mCurrent Directory Doesn't Exist?: {:s}\033[0m".format(cwd))
            
        else:
            print("\033[91mUNEXPECTED: {:s}\033[0m".format(current_line))
    
    root.calcDirectorySize()
    totalSize = root.dumpDirs()
    print("Total Size: {totalSize:d}".format(totalSize = totalSize))
    MAX_SYSTEM_SPACE = 70000000
    availableSpace = MAX_SYSTEM_SPACE - totalSize
    print("Available Space: {availableSpace:d}".format(availableSpace = availableSpace))
    PATCH_SIZE = 30000000
    neededSpace = PATCH_SIZE - availableSpace
    print("Needed Space: {neededSpace:d}".format(neededSpace = neededSpace))
    closest = root.closestButBigger(neededSpace)
    print("Closest: {closest:d}".format(closest = closest))
    #root.dumpFileSystem()