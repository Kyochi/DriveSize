import Node

class DriveOp:
    @staticmethod
    def getMo(bytesUsed):
        return (bytesUsed)/1024/1024

    @staticmethod
    def jsonBinarySearch(jsonList, attributeToCompare, elementTarget):
        start = 0
        end = len(jsonList)-1
        while (start < end):
            mid = (start+end)/2
            if ((jsonList[mid])[attributeToCompare][0] == elementTarget):
                return mid

            if ((jsonList[mid])[attributeToCompare][0] < elementTarget):
                start = mid + 1
            else:
                end = mid

        return -1

    @staticmethod
    def getIdRange(jsonList, target,  curPosition):
        targetValue = jsonList[curPosition][target][0]
        lower = curPosition
        higher = curPosition
        bounds = []
        while (jsonList[lower][target][0] ==  targetValue and lower >= 0):
            lower-=1

        while (higher <= len(jsonList)-1 and jsonList[higher][target][0] ==  targetValue):
            higher+=1

        bounds.append(lower + 1)
        bounds.append(higher-1)

        return bounds

    @staticmethod
    def dfsDriveSize(jsonList, curNode, list):

        posChild = DriveOp.jsonBinarySearch(jsonList, "parents", curNode.m_id)
        if (posChild == -1):
            curNode.m_size = float(jsonList[curNode.m_index].get('size', 0))
            return curNode.m_size

        curNode.m_childs = []
        rangeParents = DriveOp.getIdRange(jsonList, "parents", posChild)
        indexCurrentElement = rangeParents[0]

        while(indexCurrentElement <= rangeParents[1]):
            element = jsonList[indexCurrentElement]
            if (element['mimeType'].startswith("application/vnd.google-apps")):
                child = Node.Node("gdoc", 0, element['id'], element['name'], indexCurrentElement)
            else :
                child = Node.Node(element['mimeType'], 0, element['id'], element['name'], indexCurrentElement)

            curNode.m_size = curNode.m_size + DriveOp.dfsDriveSize(jsonList, child, list)
            (curNode.m_childs).append(child)
            list.append(indexCurrentElement)
            indexCurrentElement = indexCurrentElement + 1

        if (curNode.m_id == "0AAjaEAUUi370Uk9PVA"):
            sizeOfSharedElement = 0
            sharedFolder = Node.Node("application/vnd.google-apps.folder",sizeOfSharedElement, "", "SharedDocs", -1)
            sharedFolder.m_childs = []
            for indElement in set(range(len(jsonList)))- set(list):
                child = Node.Node(jsonList[indElement]['mimeType'], float(jsonList[indElement].get('size', 0)), jsonList[indElement]['id'], jsonList[indElement]['name'], indElement)
                (sharedFolder.m_childs).append(child)
                sharedFolder.m_size = sharedFolder.m_size + child.m_size
            curNode.m_size = curNode.m_size + sharedFolder.m_size
            (curNode.m_childs).append(sharedFolder)
        return curNode.m_size


