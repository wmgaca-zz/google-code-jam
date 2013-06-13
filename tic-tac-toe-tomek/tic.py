import sys

def vertical(line):
    s = set(line[:3])
    if len(s) == 1 and s[0] != '.':
        return True
    s = set(line[1:])
    if len(s) == 1 and s[0] != '.':
        return True
    return False

    if len(set(line[:3])) == 1 aor len(set(line[
    0, 1, 2
    1, 2, 3

def horizontal():
    0, 1, 2
    1, 2, 3


for i in xrange(int(sys.stdin.readline().strip())):
    # Read the game state
    matrix = [sys.stdin.readline().strip(), 
              sys.stdin.readline().strip(),
              sys.stdin.readline().strip(),
              sys.stdin.readline().strip()]

    # Empty line
    sys.stdin.readline()

    x, o, dots = False, False, False

    # Verticals

    # Horizontals

    # Diagonals
