from tree import TreeNode, Tree
import matplotlib.pyplot as plt

rootNode = TreeNode(label="age", child={
    "<30": TreeNode(label="tall", child={
        ">=170": TreeNode(
            label="accept"
        ), "<170": TreeNode(
            label="deny"
        )
    }), ">=30": TreeNode(label="deny")
})
topY = 0.9
height = 0.25
endX = 0.9
startX = 0.1
tree = Tree(rootNode)

nodeStyle = dict(boxstyle='round4', fc='#c8dcc8')
leafStyle = dict(boxstyle='sawtooth', fc='#cab3f0')


class Plotter(object):
    def __init__(self):
        self.ax1 = plt.subplot(1, 1, 1, frameon=True)

    def setTree(self, tree):
        self.tree = tree

    def plotAnnotate(self, label, xy=(), xytext=(), bbox={}):
        self.ax1.annotate(label, xy, xytext, va='center', ha='center', bbox=bbox, arrowprops={'arrowstyle': '<-'})

    def plotNode(self, parentNode, parentXy=(), childXy=(), hasLeft = False, text=""):
        print("hasLeft = "+hasLeft.__str__()+"; value = " + parentNode.label + "; parent = " + parentXy.__str__() + "; child = " + childXy.__str__())
        if parentNode.isLeaf():
            style = leafStyle
        else:
            style = nodeStyle
        self.plotAnnotate(parentNode.label, parentXy, childXy, style)
        self.plotText(parentXy, childXy, text)
        if parentNode.isLeaf():
            "empty"
            print('end')
            # xytext = (parentXy[0] - horizontalOffset + 0 * 2 * horizontalOffset, parentXy[1] - height)
            # self.plotAnnotate(value.label, xy, xytext)
        else:
            # "has child"
            # self.plotAnnotate(treeNode.getRightChild().label,
            #                   xy=(parentXy[0], parentXy[1] - 0.16),
            #                   xytext=(parentXy[0] + horizontalOffset, parentXy[1] - height))
            index = 0
            for key, value in parentNode.child.items():
                offset = 0
                if index==1:
                    #right side
                    offset = (endX - parentXy[0]) / 2
                else:
                    offset = (startX - parentXy[0]) / 2
                # print("hasLeft = "+hasLeft.__str__()+"; offset = "+offset.__str__())
                # tight offset on Y axes
                xyParent = (childXy[0], childXy[1] - 0.03)
                xyChild = (childXy[0] + offset, childXy[1] / 2)

                self.plotNode(value, xyParent, xyChild, index==1, key)
                index = 1

    def plotText(self, start=(), end=(), text=""):
        self.ax1.text((start[0] + end[0]) / 2, (start[1] + end[1] )/ 2, text, va="center", ha="center")

    def plotRoot(self):
        # self.plotNode(xy=(0.5, topY), xytext=(0.5, topY))
        # self.plotAnnotate(self.tree.rootNode.label, xy=(0.5, topY), xytext=(0.5, topY))
        self.plotNode(self.tree.rootNode, parentXy=(0.5, topY), childXy=(0.5, topY))

    def plot(self):
        plt.show()


plotter = Plotter()
plotter.setTree(tree)
plotter.plotRoot()
plotter.plot()
