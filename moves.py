# Define colors
r, w, b, o, y, g = "R", "W", "B", "O", "Y", "G"

def cta(s):
    return [i for i in s]

# Define cube faces
front = cta("BBBBBBBBB")
up =    cta("WWWWWWWWW")
back =  cta("GGGGGGGGG")
left =  cta("RRRRRRRRR")
right = cta("OOOOOOOOO")
down =  cta("YYYYYYYYY")

def display():
    print(f"\n       {back[0]} {back[1]} {back[2]}\n       {back[3]} {back[4]} {back[5]}\n       {back[6]} {back[7]} {back[8]}\n")
    print(f"{left[0]} {left[1]} {left[2]}  {up[0]} {up[1]} {up[2]}  {right[0]} {right[1]} {right[2]}")
    print(f"{left[3]} {left[4]} {left[5]}  {up[3]} {up[4]} {up[5]}  {right[3]} {right[4]} {right[5]}")
    print(f"{left[6]} {left[7]} {left[8]}  {up[6]} {up[7]} {up[8]}  {right[6]} {right[7]} {right[8]}")
    print(f"\n       {front[0]} {front[1]} {front[2]}\n       {front[3]} {front[4]} {front[5]}\n       {front[6]} {front[7]} {front[8]}\n")
    print(f"       {down[0]} {down[1]} {down[2]}\n       {down[3]} {down[4]} {down[5]}\n       {down[6]} {down[7]} {down[8]}\n")
    print(f"========================");

# Main rotation functions
def R():
    t1, t2, t3 = front[2], front[5], front[8]
    front[2], front[5], front[8] = down[2], down[5], down[8]
    down[2], down[5], down[8] = back[2], back[5], back[8]
    back[2], back[5], back[8] = up[2], up[5], up[8]
    up[2], up[5], up[8] = t1, t2, t3

    t = right[0]
    right[0] = right[6]
    right[6] = right[8]
    right[8] = right[2]
    right[2] = t
    t = right[1]
    right[1] = right[3]
    right[3] = right[7]
    right[7] = right[5]
    right[5] = t


def L():
    t1, t2, t3 = front[0], front[3], front[6]
    front[0], front[3], front[6] = up[0], up[3], up[6]
    up[0], up[3], up[6] = back[0], back[3], back[6]
    back[0], back[3], back[6] = down[0], down[3], down[6]
    down[0], down[3], down[6] = t1, t2, t3

    t = left[0]
    left[0] = left[6]
    left[6] = left[8]
    left[8] = left[2]
    left[2] = t
    t = left[1]
    left[1] = left[3]
    left[3] = left[7]
    left[7] = left[5]
    left[5] = t


def U():
    t1, t2, t3 = front[0], front[1], front[2]
    front[0], front[1], front[2] = right[6], right[3], right[0]
    right[6], right[3], right[0] = back[8], back[7], back[6]
    back[8], back[7], back[6] = left[2], left[5], left[8]
    left[2], left[5], left[8] = t1, t2, t3

    t = up[0]
    up[0] = up[6]
    up[6] = up[8]
    up[8] = up[2]
    up[2] = t
    t = up[1]
    up[1] = up[3]
    up[3] = up[7]
    up[7] = up[5]
    up[5] = t


def D():
    t1, t2, t3 = front[6], front[7], front[8]
    front[6], front[7], front[8] = left[0], left[3], left[6]
    left[0], left[3], left[6] = back[0], back[1], back[2]
    back[0], back[1], back[2] = right[2], right[5], right[8]
    right[2], right[5], right[8] = t1, t2, t3

    t = down[0]
    down[0] = down[6]
    down[6] = down[8]
    down[8] = down[2]
    down[2] = t
    t = down[1]
    down[1] = down[3]
    down[3] = down[7]
    down[7] = down[5]
    down[5] = t


def F():
    t1, t2, t3 = up[6], up[7], up[8]
    up[6], up[7], up[8] = left[6], left[7], left[8]
    left[6], left[7], left[8] = down[2], down[1], down[0]
    down[2], down[1], down[0] = right[6], right[7], right[8]
    right[6], right[7], right[8] = t1, t2, t3

    t = front[0]
    front[0] = front[6]
    front[6] = front[8]
    front[8] = front[2]
    front[2] = t
    t = front[1]
    front[1] = front[3]
    front[3] = front[7]
    front[7] = front[5]
    front[5] = t


def B():
    t1, t2, t3 = up[0], up[1], up[2]
    up[0], up[1], up[2] = right[0], right[1], right[2]
    right[0], right[1], right[2] = down[8], down[7], down[6]
    down[8], down[7], down[6] = left[0], left[1], left[2]
    left[0], left[1], left[2] = t1, t2, t3

    t = back[0]
    back[0] = back[6]
    back[6] = back[8]
    back[8] = back[2]
    back[2] = t
    t = back[1]
    back[1] = back[3]
    back[3] = back[7]
    back[7] = back[5]
    back[5] = t

# Inverse functions
# TODO : Direct assignment instead of 3x repetitions
def Fi():
    F()
    F()
    F()

def Bi():
    B()
    B()
    B()

def Ri():
    R()
    R()
    R()

def Li():
    L()
    L()
    L()

def Di():
    D()
    D()
    D()

def Ui():
    U()
    U()
    U()