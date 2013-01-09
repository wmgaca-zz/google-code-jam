import sys

"""
1023 - 7899

1023 - 1099
x
 x
  7 * 10
   6

1100 - 1199
x
 
   
"""

def main(fpath):
    with open(fpath) as f:
        lines = [tuple(map(int, x.split())) for x in f.readlines()[1:]]

    for tcindex, line in enumerate(lines):
        a, b = int(line[0]), int(line[1])

        recycled = []

        for x in xrange(a, b + 1):
            if x < 10:
                continue

            strx = str(x)

            for i in xrange(1, len(strx)):
                first, second = strx[:i], strx[i:]

                if second.startswith('0'):
                    continue

                result = int(second + first)
                
                if b >= result > x:
                    recycled.append((x, result,))

        print 'Case #%s: %s' % (tcindex + 1, len(set(recycled)))

if __name__ == '__main__':
    main(sys.argv[1])
