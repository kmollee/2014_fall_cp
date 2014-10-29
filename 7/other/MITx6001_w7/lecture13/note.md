# Trees

## Tree definition

- A tree consists of one or more nodes
    + A node typically has a value associated with it
- Nodes are connected by braches
- A tree start with a root node
- Except for leaves, each node has one or more children
    + We refer to a node which has a child as the parent node
- In simple trees, no child has more than one parent, but the generalization(often called a graph) is also very useful

## Binary trees

- A binary tree is aspecial version of a tree, where each node has at most two children
- Binary trees are very useful when storing and searching ordered data, or when determining the best decision to make in solving many classes of problems
    + Such trees are often call decision trees

## Binary tree class

```py
class binaryTree(object):

    def __init__(self, value):
        self.value = value
        self.rightBranch = None
        self.leftBranch = None
        self.parent = None

    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, parent):
        self.parent = parent

    def __str__(self):
        return self.value
```

## Searching a tree

- Imagine we want to examine a tree
    + To determine if an element is present
    + To find a path to a solution point
    + To make a series of decisions to reach some objective
- Depth first search
    + Start with the root
    + At any node, if we haven't reached our objective, take the left branch first
    + When get to a leaf, backtrack to the first decision point and take the right branch
- Breadth first search
    + Start with root
    + Then proceed to each child at the next level, in order
    + Continue until reach objective

## Depth first search for containment

- Idea is to keep a data structure(called a stack) that holds nodes still to be explored
- Use an evalution function to determine when reach obective(i.e. for containment, whether value of node is equal to desired value)
- Start with the root node
- Then add children, if any, to front of data structure, with left branch first
- Continue in ths manner

## Depth first search for path

- Suppose we want to find the actual path from root node to desired node
- A simple change in the code lets us trace back up the tree, once we find the desired node

```py
def DFSBinaryPath(root, fcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return TracePath(stack[0])
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False


def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent())
```

## Ordered search

- Suppose we know that the tree is ordered, meaning that for any node, all the nodes to the "left" are less than node's value, and all the nodes to the "right" are greater than that node's value

## Decision Trees

- A decision tree is a special type of binary tree(though could be more general tree with multiple children)
- At each node, a decision is made, with a postive decision taking the left branch, and a negative decision taking the right branch
- When we reach a node that satisfies some goal, the path back to the root node defines the solution to the problem captured by the tree

## Building a decision tree

- One way to approach decision trees is to construct an actual tree, then search it
- An alternative is to implicitly build the tree as needed
- As an example, we will build a decision tree for a [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)

## The knapsack Problem

- Suppose we are given a set of objects, each with a value and a weight
- We have a finite sized knapsack, into which we want to store some of the items
- We want to store the items that have the most value, subject to the constraint that there is a limit to the cumulative size that will fit

## Building a decision tree

- For the knapsack problem, we can build a decision tree as follows:
    + At the root level, we decide whether to include the first element(left branch) or not (right branch)
    + At the `nth` level, we make te same decision for the `nth` element
    + By keeping track of what we have included so far, and what we have left to consider, we can generate a binary tree of decisions

## Decision Trees

- Depth first and breadth first sitll search the same number of nodes, the oder is simply different
- If we are willing to settlte for `good enough`, then there is a difference in work done by the two search methods

## Searching a decision tree

```py
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


def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                prin(best.getValue())
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                prin(best.getValue())
            if stopFcn(best.getValue()):
                prin('visited', visited)
                return best
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print('visited', visited)
    return best
```

## Testing "good enough"

```py
def atLeast15(lst):
    return sumValues(lst) >= 15

print('')
print('DFS decision tree good enough')
foobar = DFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
                            atLeast15)
print(foobar.getValue())

print('')
print('BFS decision tree good enough')
foobarnew = BFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
                               atLeast15)
print(foobarnew.getValue())
```

## Searching an implicit tree

- Our approach is inefficicent, as it constructs the entire decision tree, and then searches it
- An alternative is only generate the nodes of the tree as needed
- Here is an example for the case of a knapsack problem, the same idea could be captured in other search problems


## Implicit search for knapsack

```py
def DTImplicit(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0][1] > avail:
        result = DTImplicit(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = DTImplicit(toConsider[1:], avail - nextItem[1])
        withVal += nextItem[0]
        withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
```

## What if our trees are overgrown

- We have been explicit assuming that there are no `loops` in our trees, i.e. that a child has one parent, and that no node is that parent of a child closer to the root
- What if we relax this constraint?
- Generalization is called a graph
    + Lots of great graph search problems
    + For now we can think about ways to support search for binary trees that might have loops
## Searching these "trees"

- What happens if we run depth first search on this?

```txt
An infiinite loop in manay cases when item present, and always if item not present
```

- What happens if we run breadth first search on this?

```txt
Inefficient as repeat nodes, but still works if item present, infinite loop if not present
```


## Avoiding loops

```py
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
```
