import sys

count = 0

def quick_test(needle, haystack):
    for c in needle:
        if c not in haystack:
            return False
    return True

def test(needle, haystack):
    for h in haystack:
        if h == needle[0]:
            needle = needle[1:]
        if not len(needle):
            return True
    return 0 == len(needle)

def search(needle, haystack):
    print '%s -> %s' % (needle, haystack)

    if len(needle) > len(haystack):
        return 0
    if not needle and not haystack:
        return 0
    if len(needle) == 1:
        print '  haystack.count(needle) = %s' % haystack.count(needle)
        return haystack.count(needle)
    if len(needle) == len(haystack):
        return 1 if needle == haystack else 0
    if needle == haystack:
        return 1

    if not quick_test(needle, haystack):
        return 0
    if not test(needle, haystack):
        return 0

    count = 0

    if len(needle) > 1:
        for index, h in enumerate(haystack):
            if h == needle[0]:
                if 1 == len(needle[1:]):
                    count += haystack[index + 1:].count(needle[1:])
                    print "+ cs"
                else:
                    count += search(needle[1:], haystack[index + 1:])
    
    return count
    
def main():
    lines = [line.strip() for line in sys.stdin.readlines()[1:]]

    needle = "welcome to code jam"

    for index, line in enumerate(lines[:1]):
        print line
        line = ''.join([c for c in line if c in needle])
        print line
        print "Case #%s: %.4d" % (index + 1, search(needle, line))

if __name__ == '__main__':
    main()
