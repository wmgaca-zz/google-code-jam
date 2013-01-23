import sys

values = {}

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
    if (needle, haystack) in values:
        return values[(needle, haystack)]

    if len(needle) > len(haystack): 
        return 0
    elif not needle and not haystack:
        return 0
    elif len(needle) == 1:
        return haystack.count(needle)
    elif len(needle) == len(haystack):
        return 1 if needle == haystack else 0
    elif needle == haystack:
        return 1
    #if not quick_test(needle, haystack):
    #    return 0
    #if not test(needle, haystack):
    #    return 0

    count = 0
    for index, h in enumerate(haystack):
        if h == needle[0]:
            count += search(needle[1:], haystack[index + 1:])
            count %= 10000

    global values
    values[(needle, haystack)] = count

    return count
    
def main():
    lines = [line.strip() for line in sys.stdin.readlines()[1:]]

    global values
    needle = "welcome to code jam"

    for index, line in enumerate(lines):
        values = {}

        line = ''.join([c for c in line if c in needle])
        print "Case #%s: %.4d" % (index + 1, search(needle, line) % 10000)

if __name__ == '__main__':
    main()
