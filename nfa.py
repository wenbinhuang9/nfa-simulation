## definiton of nfa
from collections import defaultdict

EPSILON = "epsilon"

def mergeOR(nfa_list):
    redefine_nfa_list = [nfa_obj.redefine_states(str(i)) for i, nfa_obj in enumerate(nfa_list)]

    nfa_obj = NFA().startState(0).acceptState(1).append(redefine_nfa_list)

    for subnfa in redefine_nfa_list:
        nfa_obj.addTransitions(nfa_obj.start, EPSILON, subnfa.start)
        nfa_obj.addTransitions(subnfa.accept, EPSILON, nfa_obj.accept)

    return nfa_obj

def mergeConcatenation(nfa_list):
    redefine_nfa_list = [nfa_obj.redefine_states(str(i)) for i, nfa_obj in enumerate(nfa_list)]

    new_nfa = redefine_nfa_list[0].append(redefine_nfa_list[1:])
    pre_nfa = new_nfa
    for i in range(1, len(redefine_nfa_list)):
        each_nfa = redefine_nfa_list[i]
        new_nfa.addTransitions(pre_nfa.accept, EPSILON, each_nfa.start)

        pre_nfa = each_nfa
        if i == len(redefine_nfa_list) - 1:
            new_nfa.accept = each_nfa.accept

    return new_nfa

def mergeStar(nfa):
    nfa.addTransitions(nfa.accept, EPSILON, nfa.start)

    return nfa


# how to generate code according to NFA definition??? there should be some algorithms
class NFA():
    def __init__(self):
        self.start = None
        self.accept = None
        ## (state, symbol)->list of states
        self.transitions = defaultdict(list)
        self.states = set([])

        ## state->list of symbols reaching out
        self.state_out = defaultdict(set)

    def isAcceptState(self, q):
        return  q in self.accept


    def startState(self, start):
        if isinstance(start, int):
            start = str(start)

        self.start = start
        self.states.add(start)
        return self

    def acceptState(self, accept):
        if isinstance(accept, int):
            accept = str(accept)
        self.accept = accept
        self.states.add(accept)

        return self

    ## q1 accepting s , go to q2
    def addTransitions(self, q1, s, q2):
        if isinstance(q1, int):
            q1 = str(q1)
        if isinstance(q2, int):
            q2 = str(q2)

        self.states.add(q1)
        self.states.add(q2)

        self.state_out[q1].add(s)

        self.transitions[(q1, s)].append(q2)

        return self


    def nextState(self, q, s):
        next = self.transitions[(q, s)]

        return next
    def nextStates(self, q):
        symbol_list = self.state_out[q]
        ans = []
        for symbol in symbol_list:
            ans.extend(self.transitions[(q, symbol)])
        return ans

    def nextSymbols(self, q):
        return self.state_out[q]





