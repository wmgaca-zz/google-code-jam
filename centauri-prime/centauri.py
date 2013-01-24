import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def run(name):
    ruler = 'a king'
    last = name[-1].lower()

    if last == 'y': ruler = 'nobody'
    elif last in vowels: ruler = 'a queen'

    return ruler

for index, line in enumerate([x.strip() for x in sys.stdin.readlines()[1:]]):
    print 'Case #%d: %s is ruled by %s.' % (index + 1, line, run(line))

