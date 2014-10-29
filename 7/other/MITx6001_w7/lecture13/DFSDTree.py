from buildDTree import buildDTree
from testfunction import *


def DFSDTree(root, valueFcn, constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                print(best.getValue())
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                print(best.getValue())
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
        else:
            queue.pop(0)
    print('visited', visited)
    return best

if __name__ == '__main__':
    a = [6, 3]
    b = [7, 2]
    c = [8, 4]
    d = [9, 5]

    treeTest = buildDTree([], [a, b, c, d])

    print('')
    print('DFS decision tree')
    foobar = DFSDTree(treeTest, sumValues, WeightsBelow10)
    print(foobar.getValue())
