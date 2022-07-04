# Code adapted from https://gist.github.com/EntilZha/5397c02dc6be389c85d8

from collections import namedtuple

Entry = namedtuple('Task', 'Hash ID Description')


class HashTable(object):

    def __init__(self):
        self.size = 0
        self.capacity = 5
        self.T = []
        for i in range(self.capacity):
            self.T.append([])

    def HashFunction(self, key):
        return key % self.capacity

    def insert(self, key, data):
        # check for existing ID
        for j in self.T:
            if len(j) > 0:
                if key == j[1]:
                    print("ID is already in use.")
                    return
            else:
                continue

        index = self.HashFunction(key)
        i = 1
        while len(self.T[index]) > 0:
            print(i)
            # Quadratic probing implementation
            index = (self.HashFunction(key) + i ** 2) % self.capacity
            i += 1
        task = Entry(index, key, data)
        self.T[index] = task
        self.size += 1

        # when hashtable is 70% filled, double in size
        if self.size >= self.capacity*0.7:
            for i in range(self.capacity):
                self.T.append([])
            self.capacity *= 2

    def getTask(self, key):
        if self.size == 0:
            print("No tasks found.\n")
            return
        for t in self.T:
            if len(t) == 0:
                continue
            if t[1] == key:
                print("Hash: {}, ID: {}, Description: {}\n".format(t[0], t[1], t[2]))
                return
        print("ID not found.\n")

    def displayHashTable(self):
        for i in range(self.capacity):
            if len(self.T[i]) == 0:
                print("table[{}]".format(i))
                continue
            else:
                print("table[{}] Hash: {}, ID: {}, Description: {}".format(i, self.T[i][0], self.T[i][1], self.T[i][2]))


h = HashTable()
while True:
    try:
        c = int(input("1. Enter a new task\n2. Retrieve a task\n3. Exit\n"))
    except ValueError:
        print("Please choose a valid task.\n")
        continue
    if c == 3:
        break
    elif c == 1:
        new = input("Enter a new task with format [ID, Description]: ")
        ent = new.split(", ")
        if len(ent) != 2:
            print("Please enter the task in a valid format.")
            continue
        try:
            if int(ent[0]) < 0:
                print("Please use an ID larger than 1.")
        except ValueError:
            print("Please enter an integer for task ID.\n")
            continue
        h.insert(int(ent[0]), ent[1])

    elif c == 2:
        if h.size == 0:
            print("No tasks found.\n")
            continue
        new = int(input("Enter a task ID: "))
        h.getTask(new)
    elif c == 4:
        h.displayHashTable()
    else:
        print("Please pick a valid task.\n")
