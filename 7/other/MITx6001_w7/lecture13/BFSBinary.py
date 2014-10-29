from binaryTree import binaryTree
from testfunction import *


def BFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print('at node ' + str(queue[0].getValue()))
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False


# if we wanted to return the path that got to the goal, would need to modify

def DFSBinaryPath(root, fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return TracePath(queue[0])
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
    return False


def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent())


if __name__ == '__main__':
    n5 = binaryTree(5)
    n2 = binaryTree(2)
    n1 = binaryTree(1)
    n4 = binaryTree(4)
    n8 = binaryTree(8)
    n6 = binaryTree(6)
    n7 = binaryTree(7)
    n3 = binaryTree(3)

    n5.setLeftBranch(n2)
    n2.setParent(n5)
    n5.setRightBranch(n8)
    n8.setParent(n5)
    n2.setLeftBranch(n1)
    n1.setParent(n2)
    n2.setRightBranch(n4)
    n4.setParent(n2)
    n8.setLeftBranch(n6)
    n6.setParent(n8)
    n6.setRightBranch(n7)
    n7.setParent(n6)
    n4.setLeftBranch(n3)
    n3.setParent(n4)

    # test examples

    print('BFS')
    BFSBinary(n5, find6)

    print('')
    print('DFS path')
    pathTo6 = DFSBinaryPath(n5, find6)
    print([e.getValue() for e in pathTo6])
