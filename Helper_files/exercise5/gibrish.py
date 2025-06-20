class gibrish:
    def __init__(self, q, w):
        self.some = q
        self.thing = w
        self. c = 0
        self.structure = []
        self.iter = []

    def addRoot(self, tree):
        if len(self.structure) >= self.some:
            raise IndexError("Max number of trees reached.")
        root = TreeNode(tree, self.thing)
        self.structure.append(root)
        self.iter.append(TreeIterator(root))

    def moveforward(self):
        if self. c < len(self.structure) - 1:
            self. c += 1
        else:
            raise IndexError("Already at the last tree.")

    def moveback(self):
        if self. c > 0:
            self. c -= 1
        else:
            raise IndexError("Already at the first tree.")

    def addLeft(self, value):
        self.iter[self. c].current.add_left(value)

    def addRight(self, value):
        self.iter[self. c].current.add_right(value)
    def goLeft(self):
        self.iter[self.c].go_left()

    def goRight(self):
        self.iter[self.c].go_right()

    def goUp(self):
        self.iter[self.c].go_up()

    def print(self):
        if len(self.structure) == 0:
            print("None")
        else:
            print(self.iter[self.c].get_value())
   

class TreeNode:
    def __init__(self, value, max_depth, depth=0, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth
        self.max_depth = max_depth
        self.parent = parent  # new

    def add_left(self, value):
        if self.depth + 1 > self.max_depth:
            raise ValueError("Max depth exceeded")
        if self.left:
            raise ValueError("Left child already exists")
        self.left = TreeNode(value, self.max_depth, self.depth + 1, parent=self)

    def add_right(self, value):
        if self.depth + 1 > self.max_depth:
            raise ValueError("Max depth exceeded")
        if self.right:
            raise ValueError("Right child already exists")
        self.right = TreeNode(value, self.max_depth, self.depth + 1, parent=self)


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

    def go_up(self):
        if self.current.parent:
            self.current = self.current.parent
        else:
            raise ValueError("No parent (already at root)")

    def get_value(self):
        return self.current.value


try:
    run_tests()
except Exception as e:
    print("Test failed:", e)
