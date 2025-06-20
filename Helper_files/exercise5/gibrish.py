class gibrish:
    def __init__(self, q, w):
        self.max = q
        self.depth = w
        self.index = 0
        self.structure = []
        self.iter = []

    def addRoot(self, tree):
        if len(self.structure) >= self.max:
            raise IndexError("Max number of trees reached.")
        root = TreeNode(tree, self.depth)
        self.structure.append(root)
        self.iter.append(TreeIterator(root))

    def moveforward(self):
        if self.index < len(self.structure) - 1:
            self.index += 1
        else:
            raise IndexError("Already at the last tree.")

    def moveback(self):
        if self.index > 0:
            self.index -= 1
        else:
            raise IndexError("Already at the first tree.")

    def addLeft(self, value):
        self.iter[self.index].current.add_left(value)

    def addRight(self, value):
        self.iter[self.index].current.add_right(value)


class TreeNode:
    def __init__(self, value, max_depth, depth=0):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth
        self.max_depth = max_depth

    def add_left(self, value):
        if self.depth + 1 > self.max_depth:
            raise ValueError("Max depth exceeded")
        if self.left:
            raise ValueError("Left child already exists")
        self.left = TreeNode(value, self.max_depth, self.depth + 1)

    def add_right(self, value):
        if self.depth + 1 > self.max_depth:
            raise ValueError("Max depth exceeded")
        if self.right:
            raise ValueError("Right child already exists")
        self.right = TreeNode(value, self.max_depth, self.depth + 1)


class TreeIterator:
    def __init__(self, root):
        self.current = root

    def go_left(self):
        if self.current.left:
            self.current = self.current.left
        else:
            raise ValueError("No left child")

    def go_right(self):
        if self.current.right:
            self.current = self.current.right
        else:
            raise ValueError("No right child")

    def get_value(self):
        return self.current.value
def run_tests():
    print("Creating a gibrish manager with max 2 trees and max depth 2...")
    manager = gibrish(2, 2)

    print("Adding first root node with value 'A'...")
    manager.addRoot("A")

    print("Adding left and right children to root 'A'...")
    manager.addLeft("B")
    manager.addRight("C")

    print("Moving iterator to left child of 'A'...")
    manager.iter[manager.index].go_left()
    print("Current node value:", manager.iter[manager.index].get_value())  # Should print 'B'

    print("Moving iterator back to root...")
    manager.iter[manager.index] = TreeIterator(manager.structure[manager.index])  # Reset iterator

    print("Moving iterator to right child of 'A'...")
    manager.iter[manager.index].go_right()
    print("Current node value:", manager.iter[manager.index].get_value())  # Should print 'C'

    print("Adding second root node with value 'X'...")
    manager.addRoot("X")

    print("Moving to the second tree...")
    manager.moveforward()
    print("Current tree root:", manager.iter[manager.index].get_value())  # Should print 'X'

    print("Trying to add left child to 'X'...")
    manager.addLeft("Y")
    print("Navigating to left child...")
    manager.iter[manager.index].go_left()
    print("Current node value:", manager.iter[manager.index].get_value())  # Should print 'Y'

    print("All tests passed without exception.")

try:
    run_tests()
except Exception as e:
    print("Test failed:", e)
