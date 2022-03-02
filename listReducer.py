# def reduce(x):
#     final = []
#     i = 0
#     flag = True
#     while i < len(x) - 1:
#         if x[i] == x[i+1]:
#             final.append(x[i] + "2")
#             i+=1
#         else:
#             final.append(x[2])
#         i+=1
#     return final
# test = ['R', 'R', 'L', 'F', 'F', 'F', 'F']
# print(reduce(test))

def reducer(x):
    def z(a, reg, newGuy = ""):
        return a.replace(reg, newGuy)
    y = ""
    while x is not y:
        print(x)
        y = x
        nullString = ["LiL", "LLi", "RiR", "RRi", "FiF", "FFi", "BiB", "BBi", "DiD", "DDi", "UiU", "UUi", "R2R2", "L2L2", "F2F2", "D2D2", "U2U2", "B2B2"]
        # twos = ["LL", "RR", "BB", "UU", "FF", "DD", "LiLi", "RiRi", "DiDi", "BiBi", "UiUi", "FiFi"]
        triple = ["LLL", "LiLiLi", "RRR", "RiRiRi", "DDD", "DiDiDi", "UUU", "UiUiUi", "BBB", "BiBiBi", "FFF", "FiFiFi"]
        for n in nullString:
            x = z(x, n)
        for t in triple:
            x = z(x, t, t[0] if len(t) == 6 else t[0] + 'i')

    print(x)
    return x

t = "RDDDD"
finalList = reducer(t)
print(f'{finalList = }')