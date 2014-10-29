from binaryTree import binaryTree
from testfunction import *


def DFSBinaryNoLoop(root, fcn):
    queue = [root]
    seen = []
    while len(queue) > 0:
        print('at node ' + str(queue[0].getValue()))
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            seen.append(temp)
            if temp.getRightBranch():
                if not temp.getRightBranch() in seen:
                    queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                if not temp.getLeftBranch() in seen:
                    queue.insert(0, temp.getLeftBranch())
    return False


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
    n3.setLeftBranch(n5)
    n5.setParent(n3)

    print(DFSBinaryNoLoop(n5, find6))
