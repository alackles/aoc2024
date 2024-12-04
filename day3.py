import re

line = ""

with open("toy.txt") as f:
    for ln in f.readlines():
        line += ln.strip()

enabled = []

parts = line.split('don\'t()')
enabled.append(parts[0])

for part in parts[1:]:
    valid = part.split('do()')
    for v in valid[1:]:
        enabled.append(v)


newline = "".join(enabled)

mults = re.findall(r'mul\(\d+,\d+\)', newline)

tot = 0

for mult in mults:
    x = int(re.search(r'\((\d+),', mult).group(1))
    y = int(re.search(r',(\d+)\)', mult).group(1))
    tot += x*y

print(tot)
