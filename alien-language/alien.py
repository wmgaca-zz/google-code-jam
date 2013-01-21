import sys

def translate(pattern):
    output = []
    current = ''
    buffer_chars = False

    for char in pattern:
        if char == '(':
            buffer_chars = True
        elif char == ')':
            buffer_chars = False
            if current:
                output.append(current)
                current = []
        elif buffer_chars:
            current += char
        else:
            output.append(char)

    return output

def match(pattern, word):
    for left, right in zip(pattern, word):
        if right not in left:
            return False
    return True

def main():
    L, D, N = tuple(map(int, sys.stdin.readline().split()))
    lines = sys.stdin.readlines()
    words = [word.strip() for word in lines[:D]]
    tests = [translate(test.strip()) for test in lines[D:]]

    for index, test in enumerate(tests):
        matched = 0
        for word in words:
            if match(test, word):
                matched += 1
        print 'Case #%s: %s' % (index + 1, matched)
        

if __name__ == '__main__':
    main()
