from sys import stdin

#Eat the first line
stdin.readline()

def count_prefixes(prefixes, position):
    return sum(i[1] for i in prefixes if i[0] < position)

def count_text(line, text):
    curr =[(-1, 1)]
    for c in text:
        curr = [(i, count_prefixes(curr, i))
                 for i, d in enumerate(line) if d == c]
    return sum(i[1] for i in curr)

for i, line in enumerate(l.strip() for l in stdin.readlines()):
    print "Case #%d %04d"%(i + 1, count_text(line, "welcome to code jam"))

