file1 = open('shared/input_day_03.txt', 'r') 
Lines = file1.readlines() 
  


def part_01(right: int, down: int):
    count_r = 0
    count_d = 0
    trees = 0
    for line in Lines: 
        line = line.strip()
        r = count_r * right
        d = count_d % down
        length = line.__len__()
        t = (r / length) + 1
        t = t.__int__()
        rr = r % length
        count_d = count_d + 1
        if d!=0:
            continue
        count_r = count_r + 1
        if line[rr]=="#":
            trees = trees + 1
        #print(line)
        #print(line[rr])
        #print(" "*rr + line[rr])
    return trees
    
print(part_01(1, 1))
print(part_01(3, 1))
print(part_01(5, 1))
print(part_01(7, 1))
print(part_01(1, 2))
product = part_01(1, 1) * part_01(3, 1) * part_01(5, 1) * part_01(7, 1) * \
    part_01(1, 2)
print(product)