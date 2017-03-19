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

        while (jsonList[higher][target][0] ==  targetValue and higher < len(jsonList)-1):
            higher+=1

        bounds.append(lower + 1)
        bounds.append(higher)

        return bounds

    @staticmethod
    def dfsDriveSize(jsonList, curNode):

        posChild = DriveOp.jsonBinarySearch(jsonList, "parents", curNode.m_id)
        if (posChild == -1):
            if (curNode.m_type != 'gdoc'):
                curNode.m_size = float((jsonList[curNode.m_index])['size'])
                return curNode.m_size
            else:
                return 0

        curNode.m_childs = []
        rangeParents = DriveOp.getIdRange(jsonList, "parents", posChild)
        indexCurrentElement = rangeParents[0]
        for element in jsonList[rangeParents[0]: rangeParents[1]]:
            if (element['mimeType'].startswith("application/vnd.google-apps")):
                child = Node.Node("gdoc", 0, element['id'], element['name'], indexCurrentElement)
            else :
                child = Node.Node(element['mimeType'], 0, element['id'], element['name'], indexCurrentElement)

            curNode.m_size = curNode.m_size + DriveOp.dfsDriveSize(jsonList, child)
            (curNode.m_childs).append(child)
            indexCurrentElement = indexCurrentElement + 1

        return curNode.m_size


