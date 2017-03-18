import Node

class DriveOp:
    @staticmethod
    def getMo(self, bytesUsed):
        return int(bytesUsed)/1024/1024

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

        while (jsonList[higher][target][0] ==  targetValue and higher < len(jsonList)):
            higher+=1

        bounds.append(lower + 1)
        bounds.append(higher - 1)

        return bounds

    @staticmethod
    def dfsDriveSize(jsonList, curNode):
        posChild = DriveOp.jsonBinarySearch(jsonList, "parents", curNode.m_id)
        if (posChild == -1):
            if (curNode.m_type != 'gdoc'):
                index = DriveOp.jsonBinarySearch(jsonList, "id", curNode.m_id)
                return DriveOp.getMo((jsonList[index])['size'])
            else:
                return 0

        rangeParents = DriveOp.getIdRange(jsonList, "parents", posChild)
        for element in jsonList[rangeParents[0]: rangeParents[1]]:
            if (element['mimeType'].startswith("application/vnd.google-apps")):
                child = Node.Node("gdoc", 0, element['id'], element['name'])
            else :
                child = Node.Node(element['mimeType'], 0, element['id'], element['name'])

            curNode.m_size = curNode.m_size + DriveOp.dfsDriveSize(jsonList, child)
            (curNode.m_childs).append(child)



