import sys
import gc

# Enable automatic garbage collection
gc.enable()

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    def __del__(self):
        print(f"{self.name} is being garbage collected")


# Step 1: Create Nodes

A = Node("Node A")
B = Node("Node B")


# Step 2: Create Circular Reference

A.link = B
B.link = A

print("Cycle created:")
print("A ->", A.link.name)
print("B ->", B.link.name)


# Step 3: Check Reference Counts

print("\nReference Counts:")
print("Ref count of A:", sys.getrefcount(A))
print("Ref count of B:", sys.getrefcount(B))


# Step 4: Store object IDs

a_id = id(A)
b_id = id(B)


# Step 5: Delete Direct References

del A
del B

print("\nDeleted A and B variables.")


# Step 6: Investigate Garbage Collector

print("\nObjects still tracked by GC before collection:")

found = False
for obj in gc.get_objects():
    if id(obj) == a_id or id(obj) == b_id:
        print("Found unreachable object still in memory:", obj)
        found = True

if not found:
    print("Objects not found.")


# Step 7: Force Garbage Collection

print("\nRunning Garbage Collector...")

collected = gc.collect()

print("Unreachable objects collected:", collected)


# Step 8: Verify Cleanup

print("\nObjects still tracked after collection:")

found_after = False
for obj in gc.get_objects():
    if id(obj) == a_id or id(obj) == b_id:
        print("Object still exists:", obj)
        found_after = True

if not found_after:
    print("Cycle cleaned successfully.")