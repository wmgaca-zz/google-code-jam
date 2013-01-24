import sys

def match(pattern, titles):
    for title in titles:
        if pattern in title.lower():
            return True
    return False

def test(title, titles):
    for t in titles:
        if title in t:
            return False
    return True

def doit(title, titles):
    if not len(titles): return '""'
    if not test(title, titles): return ':('

    patterns = []
    for l in xrange(1, len(title) + 1):
        for i in xrange(len(title) - l + 1):
            pattern = title[i:i+l].lower()
            if not match(pattern, titles):
                patterns.append(pattern)
        if len(patterns):
            break

    if len(patterns) > 1:
        patterns = sorted(patterns)

    return '"%s"' % patterns[0].upper()

T = int(sys.stdin.readline().strip())
for t in xrange(T):
    N = int(sys.stdin.readline().strip())
    titles = [sys.stdin.readline().strip() for x in xrange(int(N))]
    print "Case #%d:" % (t + 1)
    for i in xrange(len(titles)):
        print '%s' % doit(titles[i], titles[:i] + titles[i+1:])
    
