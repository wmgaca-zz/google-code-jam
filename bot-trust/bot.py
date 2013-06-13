import sys

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return [int(x.strip()) for x in stdreadline().split()]

O = 'O'
B = 'B'

moves = None

def getnext(bot, current):
    if current > len(moves): return None

    for x in xrange(current, len(moves)):
        if moves[x][0] == bot: return x

    return None

T = stdreadint()
for t in xrange(1, T+1):
    global moves
    moves = [x.strip() for x in stdreadline().strip().split()[1:]]
    moves = zip(moves[::2], map(lambda x: int(x) - 1, moves[1::2]))
    count = 0

    omoves = [m for m in moves if m[0] == O]
    bmoves = [m for m in moves if m[0] == B]

    opos = 0
    bpos = 0

    while len(moves):
        bdone = False
        odone = False

        # Move?
        if opos != omoves[0][1]:
            opos += 1 if opos < omoves[0][1] else -1
            odone = True
        if bpos != bmoves[0][1]:
            bpos += 1 if bpos < bmoves[0][1] else -1
            bdone = True

        if moves[0][0] == O and not odone:
            pass

        if moves[0][0] == B and not bdone:




        # Press?
        if moves[0] in [omoves[0], bmoves[0]]:
            if moves[0] == omoves[0]:
                moves.pop(0)
                omoves.pop(0)
                odone = True
            else moves[0] == bmoves[0]:
                moves.pop(0)
                bmoves.pop(0)
                bdone = True

        # Move?
        if not bdone and 

        count += 1



    print 'Case #%s: %s' % (t, count)
    print moves
    break
