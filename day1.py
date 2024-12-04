l1 = []
l2 = []

with open("input.txt") as f:
    for line in f.readlines():
        first, second = line.split()
        l1.append(int(first))
        l2.append(int(second))

l1 = sorted(l1)
l2 = sorted(l2)

listsum = 0
simscore = 0

for i in range(len(l1)):
    listsum += abs(l1[i]-l2[i])
    simscore += l1[i] * l2.count(l1[i])

print(listsum)
print(simscore)