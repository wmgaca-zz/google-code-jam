import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def count_vowels(s):
    count = 0
    for v in vowels:
        count += s.count(v)
    return count

def process(spell):
    candidates = []

    for l in xrange(1, len(spell) + 1):
        candidates.append([])
        for i in xrange(len(spell) - l + 1):
            candidate = spell[i:i+l]
            if count_vowels(candidate) == 2 and spell.count(candidate) > 1: 
                candidates[-1].append((i, candidate,))

    for c in candidates:
        for i1, p1 in c:
            for i2, p2 in c:
                if i1 == i2 or p1 != p2: continue

                start, end = (i1, i2) if i1 < i2 else (i2, i1)
                l = len(p1)

                word = spell[start+l:end]

                if count_vowels(word): return True

    return False

for index, line in enumerate([s.strip() for s in sys.stdin.readlines()[1:]]):
    print 'Case #%d: %s' % (index + 1, 'Spell!' if process(line) else 'Nothing.')

