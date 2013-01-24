import sys
import collections

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return [int(x.strip()) for x in stdreadline().split()]

def process(day, monks):
    whispered, heard = set(), set()
    whispering = set([day])
    while True:
        if not whispering: break
        for w in whispering:
            heard.add(w)
            whispered.add(w)
            if w in monks:
                heard = heard.union(monks[w])
                whispering = whispering.union(monks[w])
        whispering -= whispered
    return len(whispered)

T = stdreadint()
for t in xrange(1, T+1):
    N = stdreadint()
    
    monks = collections.defaultdict(set)

    for f, val in enumerate(stdreadints(), start=1):
        monks[val].add(f)
    
    print 'Case #%d:' % (t)
    for day in xrange(1, N+1):
        print process(day, monks)
        
