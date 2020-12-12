import fileinput

DEBUG = True


def debug(*args):
    if DEBUG:
        print(*args)


lobby = [line.strip() for line in fileinput.input()]

answer = 0


def debug_lobby(lobby):
    debug('\n'.join(lobby))


debug_lobby(lobby)

debug('---- DEBUG ENDS ----')

print(answer)
