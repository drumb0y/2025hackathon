class gibrish:
    def __init__(self, q, w):
        self.some = q
        self.thing = w
        self. c = 0
        self.list = []
        self.readers = []

    def begin(self, v):
        if len(self.list) >= self.some:
            raise IndexError("No it is not time yet")
        n = TreeNode(v, self.thing)
        self.list.append(n)
        self.readers.append(TreeIterator(n))

    def left(self):
        if self. c < len(self.list) - 1:
            self. c += 1
        else:
            raise IndexError("Already at the last tree.")

    def right(self):
        if self. c > 0:
            self. c -= 1
        else:
            raise IndexError("Already at the first tree.")

    def mystery(self, value):
        self.readers[self. c].current.add_left(value)
    def noName (self, value):
        self.readers[self. c].current.add_right(value)
    def no(self):
        self.readers[self.c].go_left()

    def yes(self):
        self.readers[self.c].go_right()

    def up(self):
        self.readers[self.c].go_up()

    def print(self):
        if len(self.list) == 0:
            print("None")
        else:
            print(self.readers[self.c].get_value())
   

class TreeNode:
    def __init__(self, x, d, y=0, p=None):
        self.x = x
        self.qwerty = None
        self.uiop = None
        self.y = y
        self.d = d
        self.wasd = p  

    def add_left(self, t):
        if self.y + 1 > self.d:
            raise ValueError("Max depth exceeded")
        if self.left:
            raise ValueError("Left child already exists")
        self.left = TreeNode(t, self.d, self.y + 1, p=self)

    def add_right(self, t):
        if self.y + 1 > self.d:
            raise ValueError("Max depth exceeded")
        if self.uiop:
            raise ValueError("Right child already exists")
        self.uiop = TreeNode(t, self.d, self.y + 1, parent=self)


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
        return self.current.x


try:
    run_tests()
except Exception as e:
    print("Test failed:", e)
