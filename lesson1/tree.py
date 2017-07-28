class TreeNode(object):
    def __init__(self, label, child={}):
        self.label = label
        self.child = child
        # print("label = "+self.label)
    def isLeaf(self):
        return self.child is None or len(self.child)==0
    def getLeftChild(self):
        if len(self.child) > 0:
            keys = self.child.keys()
            for key in keys:
                value = self.child.get(key)
                if not value.isLeaf():
                    return value
    def getRightChild(self):
        if len(self.child) > 1:
            keys = self.child.keys()
            for key in keys:
                value = self.child.get(key)
                if value.isLeaf():
                   return value
class Tree(object):
    def __init__(self, rootNode):
        self.rootNode = rootNode

