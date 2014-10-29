# for depth and breadth tree


def find6(node):
    return node.getValue() == 6


def find10(node):
    return node.getValue() == 10


def find2(node):
    return node.getValue() == 2


def lt6(node):
    return node.getValue() > 6


# for decision tree

def sumValues(lst):
    vals = [e[0] for e in lst]
    return sum(vals)


def sumWeights(lst):
    wts = [e[1] for e in lst]
    return sum(wts)


def WeightsBelow10(lst):
    return sumWeights(lst) <= 10


def WeightsBelow6(lst):
    return sumWeights(lst) <= 6


def atLeast15(lst):
    return sumValues(lst) >= 15
