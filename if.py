class TreeNode(object):
    def __init__(self, label, child={}):
        print('construct')
        self.label = label
        self.child = child
    def isLeaf(self):
        return len(self.child) == 0

acceptNode = TreeNode("accept", None)
denyNode = TreeNode("deny", None)
moneyNode = TreeNode("money")
tallNode = TreeNode("tall")
ageNode = TreeNode("age")

ageNode.child[">=30"] = denyNode
ageNode.child["<30"] = acceptNode

def printNode(treeNode):
    print("Node:")
    print("label = "+treeNode.label)
    if not (treeNode.isLeaf()):
        print("↓")
        printNode(treeNode.child)

# printNode(ageNode)
