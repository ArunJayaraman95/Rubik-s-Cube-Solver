import copy
from timeit import default_timer as timer
# Be sure to use copy.copy()


# Define colors
r, w, b, o, y, g = "R", "W", "B", "O", "Y", "G"

# Define cube faces
front = [b]*9
back = [g]*9
left = [r]*9
right = [o]*9
up = [w]*9
down = [y]*9

def display():
    print(f"\n       {back[0]} {back[1]} {back[2]}\n       {back[3]} {back[4]} {back[5]}\n       {back[6]} {back[7]} {back[8]}\n")
    print(f"{left[0]} {left[1]} {left[2]}  {up[0]} {up[1]} {up[2]}  {right[0]} {right[1]} {right[2]}")
    print(f"{left[3]} {left[4]} {left[5]}  {up[3]} {up[4]} {up[5]}  {right[3]} {right[4]} {right[5]}")
    print(f"{left[6]} {left[7]} {left[8]}  {up[6]} {up[7]} {up[8]}  {right[6]} {right[7]} {right[8]}")
    print(f"\n       {front[0]} {front[1]} {front[2]}\n       {front[3]} {front[4]} {front[5]}\n       {front[6]} {front[7]} {front[8]}\n")
    print(f"       {down[0]} {down[1]} {down[2]}\n       {down[3]} {down[4]} {down[5]}\n       {down[6]} {down[7]} {down[8]}\n")
    print(f"========================");

def R():
    t1, t2, t3 = front[2], front[5], front[8]
    front[2], front[5], front[8] = down[2], down[5], down[8]
    down[2], down[5], down[8] = back[2], back[5], back[8]
    back[2], back[5], back[8] = up[2], up[5], up[8]
    up[2], up[5], up[8] = t1, t2, t3
    t = right[0]
    right[0] = right[3]
    right[3] = right[6]
    right[6] = right[7]
    right[7] = right[8]
    right[8] = right[5]
    right[5] = right[2]
    right[2] = right[1]
    right[1] = t


def L():
    t1, t2, t3 = front[0], front[3], front[6]
    front[0], front[3], front[6] = up[0], up[3], up[6]
    up[0], up[3], up[6] = back[0], back[3], back[6]
    back[0], back[3], back[6] = down[0], down[3], down[6]
    down[0], down[3], down[6] = t1, t2, t3
    t = right[0]
    right[0] = right[3]
    right[3] = right[6]
    right[6] = right[7]
    right[7] = right[8]
    right[8] = right[5]
    right[5] = right[2]
    right[2] = right[1]
    right[1] = t


display()
start = timer()
R()
end = timer()
print(end-start)
display()
L()
display()

# Solve White Corners

# Fix corners

# Solve edges

# OLL

# PLL

# Print List (delete later) (IMPORT MODULE)

# Condense List

# Print Final List