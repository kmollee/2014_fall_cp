from buildDTree import buildDTree
from testfunction import *


def DFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        if constraintFcn(stack[0].getValue()):
            if best == None:
                best = stack[0]
                print(best.getValue())
            elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
                best = stack[0]
                print(best.getValue())
            if stopFcn(best.getValue()):
                print('visited', visited)
                return best
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            stack.pop(0)
    print('visited', visited)
    return best

if __name__ == '__main__':
    a = [6, 3]
    b = [7, 2]
    c = [8, 4]
    d = [9, 5]

    treeTest = buildDTree([], [a, b, c, d])
    print('')
    print('DFS decision tree good enough')
    foobar = DFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
                                atLeast15)
    print(foobar.getValue())
