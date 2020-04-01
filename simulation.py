
from  nfa import  NFA, EPSILON


def getNFAStream(input):
    nfa = NFA()
    with open(input) as fd:
        lines =  fd.readlines()
        if len(lines) < 2:
            raise ValueError("invalid nfa={0}", lines)
        start = parseStart(lines[0])
        accept = parseAccept(lines[1])

        nfa.accept = accept
        nfa.start = start

        for i in range(2, len(lines)):
            q1, a, q2 = parseTransition(lines[i])
            nfa.addTransitions(q1, a, q2)

        return nfa

def parseAccept(acceptLine):
    split_arr = acceptLine.split()

    if len(split_arr) < 1:
        raise ValueError("invalid nfa={0}".format(acceptLine))
    if split_arr[0].lower() != "accept":
        raise ValueError("invalid nfa={0}".format(acceptLine))

    return split_arr[1:]


def parseStart(startLine):
    split_arr = startLine.split()

    if len(split_arr) < 1:
        raise ValueError("invalid nfa={0}".format(startLine))
    if split_arr[0].lower() != "start":
        raise ValueError("invalid nfa={0}".format(startLine))

    return split_arr[1:]


def parseTransition(transition_line):
    split_arr = transition_line.split()

    if len(split_arr) != 3:
        raise ValueError("invalid nfa={0}".format(transition_line))

    q1, a, q2 = split_arr[0], split_arr[1], split_arr[2]

    return (q1, a, q2)



def simulate(nfa, word):

    for begin in nfa.start:
        if __simulate(nfa, word, begin):
            return True

    return False

def __simulate(nfa, input, q):
    if len(input) == 0:
        return nfa.isAcceptState(q)

    symbols = nfa.nextSymbols(q)
    if symbols == None or len(symbols) == 0:
        return False

    for s in symbols:
        if s != EPSILON and input[0] == s:
            nextstates = nfa.nextState(q, s)
            if nextstates == None or len(nextstates) == 0:
                raise ValueError("invalid nfa")

            for next in nextstates:
                ans = __simulate(nfa, input[1:], next)
                if ans == True:
                    return True
        else:
            nextstates = nfa.nextState(q, EPSILON)
            for next in nextstates:
                ans = __simulate(nfa, input, next)
                if ans == True:
                    return True

    return False
