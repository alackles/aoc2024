safecount = 0


def is_safe(lst):
    # found here: https://www.reddit.com/r/adventofcode/comments/1h4ncyr/comment/m0041k3/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    inc = [lst[i] < lst[i-1] for i in range(1, len(lst))] # note that you can iterate the entire list once for the increase
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3} # all elements either 1, 2, 3 or -1, -2, -3



with open("input.txt") as f:
    for line in f.readlines():
        record = [int(x) for x in line.split()]
        if is_safe(record):
            safecount += 1
        else:
            for i in range(len(record)):
                new_record = record[0:i] + record[i+1:]
                if is_safe(new_record):
                    safecount += 1
                    break
print(safecount)