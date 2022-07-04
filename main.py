import time
import random
from BinaryTree import *
from AVLTree import *

rol = []
sl = []

while True:
    try:
        n = int(input("How many integers?\n"))
    except ValueError:
        print("Please input an integer.\n")
        continue
    if n > 1000:
        print("Please input a number less than 1000.")
        continue
    break
randint = random.sample(range(1, 1001), n)
for x in randint:
    rol.append(x)
    sl.append(x)
sl.sort()

print(rol)
print(sl)
print("\n")

rootB1 = None
for n in rol:
    rootB1 = insert(rootB1, n)
rootB2 = None
for n in sl:
    rootB2 = insert(rootB2, n)

tree1 = AVLTree()
rootA1 = None
for n in rol:
    rootA1 = tree1.insert_node(rootA1, n)
tree2 = AVLTree()
rootA2 = None
for n in sl:
    rootA2 = tree2.insert_node(rootA2, n)

print("Searching for value 2000\n")

start = time.perf_counter_ns()
s = search(rootB1, 2000)
if s is True:
    print("Value is in tree")
else:
    print("Value is not in unsorted binary tree")
print("{}ns\n".format(time.perf_counter_ns() - start))

start = time.perf_counter_ns()
s = search(rootB2, 2000)
if s is True:
    print("Value is in tree")
else:
    print("Value is not in sorted binary tree")
print("{}ns\n".format(time.perf_counter_ns() - start))

start = time.perf_counter_ns()
s = tree1.searchA(rootA1, 2000)
if s is True:
    print("Value is in tree")
else:
    print("Value is not in unsorted AVL tree")
print("{}ns\n".format(time.perf_counter_ns() - start))

start = time.perf_counter_ns()
s = tree2.searchA(rootA2, 2000)
if s is True:
    print("Value is in tree")
else:
    print("Value is not in sorted AVL tree")
print("{}ns".format(time.perf_counter_ns() - start))
