def reduce(x):
    final = []
    i = 0
    flag = True
    while i < len(x) - 1:
        if x[i] == x[i+1]:
            final.append(x[i] + "2")
            i+=1
        else:
            final.append(x[2])
        i+=1
    return final
test = ['R', 'R', 'L', 'F', 'F', 'F', 'F']
print(reduce(test))