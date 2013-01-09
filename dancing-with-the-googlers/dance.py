import sys

"""
~i:
    x   x    x    = 3x
    x   x    x-1  = 3x - 1
    x   x-1  x-1  = 3x - 2

i:
    x   x    x-2  = 3x - 2
    x   x-2  x-2  = 3x - 4
    x   x-1  x-2  = 3x - 3  (dividable by 3!)
"""

def nonsuprising(number):
    """
    a:   x   x    x    = 3x
    b:   x   x    x-1  = 3x - 1
    c:   x   x-1  x-1  = 3x - 2
    """

    best = []

    if not number % 3:
        best.append(number / 3)
    if not (number + 1) % 3:
        best.append((number + 1) / 3)
    if not (number + 2) % 3:
        best.append((number + 2) / 3)
    
    if best:
        return max(best)
    else:
        return None

def suprising(number):
    """
    d:   x   x    x-2  = 3x - 2
    e:   x   x-2  x-2  = 3x - 4
    f:   x   x-1  x-2  = 3x - 3  (dividable by 3!)
    """
    
    best = []

    if not number % 3:
        best.append(number / 3 + 1)
    if not (number + 2) % 3:
        best.append((number + 2) / 3)
    if not (number + 4) % 3:
        best.append((number + 4) / 3)
    
    if best:
        return max(best)
    else:
        return None

def main(fpath):
    with open(fpath) as f:
        tests = [test.strip().split(' ') for test in f.readlines()[1:]]

    # Pre-compute the best possible values for each score (0-30)
    nsbest = {} # dancer's nonsuprising best score
    sbest = {} # dancer's suprising best score
    for x in xrange(31):
        nsbest[x] = nonsuprising(x)
        sbest[x] = suprising(x)
    
    for index, test in enumerate(tests):
        test = [int(x) for x in test]

        N, S, p = test[:3]
        scores = test[3:]

        nsscores = 0
        sscores = 0

        for score in scores:
            if p > score:
                continue

            nsscore = nsbest[score]
            sscore = sbest[score]
        
            if nsscore is not None and nsscore >= p:
                nsscores += 1
            elif sscore is not None and sscore >= p:
                sscores += 1

        print 'Case #%s: %s' % (index + 1, nsscores + min(sscores, S))

if __name__ == '__main__':
    main(sys.argv[1])
