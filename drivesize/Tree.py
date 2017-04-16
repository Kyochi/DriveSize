from Node import Node
from DriveOp import DriveOp

class Tree:
    def __init__(self, rootid):
        self._rootId = rootid
        self._driveBuilder = DriveOp()

    def buildTree(self, files):
        self.rootFolder =  Node("application/vnd.google-apps.folder", 0, self._rootId, "rootDrive", -1)
        self._sortedFiles = sorted(files,key=lambda parent : ('parents' not in parent, parent.get('parents', [])))
        self.treesize = self._driveBuilder.dfsDriveSize(self._sortedFiles,self.rootFolder, [])

    def getSizeOf(self, size):
        return self._driveBuilder.getGo(size)