'''

E = 5
R = 2

5  6  7  10  9  1  2  3  4

N  N  2   5  N  N  N  N  N

      3   5

'''

import sys

def stdreadint():
    return int(sys.stdin.readline().strip())

def stdreadints(): 
    return map(lambda x: in t(x.strip()), 
               sys.stdin.readline().split())

for t in xrange(stdreadint()):
    E, R, N = stdreadints()
    v = stdreadints()

    if N <= 1:
        print E, R, N, '&', v, '->', N * E
        continue

    if R >= E:
        print E, R, N, '&', v, '->', sum(v) * E
        continue
    
    print E, R, N, '&', v, '-> Dunno yet.'

    # Create a value -> index dictionary
    d = dict(map(lambda x: x[::-1], enumerate(v)))

    max_energy = [None] * N

    for value in sorted(d.keys())[::-1]:
        index = d[value]
        print value, '->', index
        
        if max_energy[index] is None:
            max_energy[index] = E

        curr = 0
        for i in xrange(index + 1, N):
            curr += R
            if curr >= E:
                break
            if max_energy[i] 
            max_energy[i] = curr
            if curr >= E:
                break



        break
        
    print max_energy
    


    print d
