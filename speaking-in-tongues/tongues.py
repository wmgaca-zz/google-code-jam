import sys
import ctypes

class Palette(object):

    WHITE = 7
    GREEN = 0x02
    RED = 0x04

STD_OUTPUt_HANDLE = -11
HANDLE = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUt_HANDLE)

def stdsetcolor(color):
    ctypes.windll.kernel32.SetConsoleTextAttribute(HANDLE, color)

def stdprint(string):
    sys.stdout.write(string)

def stdcprint(string, color):
    stdsetcolor(color)
    stdprint(string)
    stdsetcolor(Palette.WHITE)

known = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
    'n': 'b',
    'f': 'c',
    'i': 'd',
    'c': 'e',
    'w': 'f',
    'l': 'g',
    'b': 'h',
    'k': 'i',
    'u': 'j',
    'o': 'k',
    'm': 'l',
    'x': 'm',
    's': 'n',
    'v': 'p',
    'z': 'q',
    'p': 'r',
    'd': 's',
    'r': 't',
    't': 'w',
    'a': 'y',
    'h': 'x',
    'j': 'u',
    'g': 'v',
    ' ': ' '
}

known_bad = known.values()

def translate(c):
    if 1 == len(c):
        return known[c]
    else:
        return ''.join([known[x] for x in c])

def printline(line):
    for c in line:
        if c in known:
            stdcprint(translate(c), Palette.GREEN)
        elif c in known_bad:
            stdcprint(c, Palette.RED)
        else:
            stdprint(c)
    stdprint('\n')

def main(fname):

    with open(fname) as f:
        lines = [line.strip() for line in f.readlines()[1:]]

    for index, line in enumerate(lines):
        print 'Case #%s: %s' % (index + 1, translate(line)) #printline(line)

if __name__ == '__main__':
	main(sys.argv[1])
