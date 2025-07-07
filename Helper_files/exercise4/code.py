def part1(t):
    add = 2
    index = 0 
    for value in t:
        if int(value) %2 == 1:
            t[index] = value+add
        else:
            t[index]= value+add
            add=(add*2)-(index*3)
        index = index +1
    return t

