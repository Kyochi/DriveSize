

class DriveOp:
    @staticmethod
    def getMoUsed(self, bytesUsed):
        return int(bytesUsed)/1024/1024

    @staticmethod
    def jsonBinarySearch(listJson, attributeToCompare, elementTarget):
        start = 0
        end = len(listJson)-1
        while (start < end):
            mid = (start+end)/2
            if ((listJson[mid])[attributeToCompare][0] == elementTarget):
                return mid

            if ((listJson[mid])[attributeToCompare][0] < elementTarget):
                start = mid + 1
            else:
                end = mid

        return -1

    @staticmethod
    def getIdRange(listJson, target,  curPosition):
        targetValue = listJson[curPosition][target][0]
        lower = curPosition
        higher = curPosition
        bounds = []
        while (listJson[lower][target][0] ==  targetValue and lower >= 0):
            lower-=1

        while (listJson[higher][target][0] ==  targetValue and higher < len(listJson)):
            higher+=1

        bounds.append(lower + 1)
        bounds.append(higher - 1)

        return bounds



