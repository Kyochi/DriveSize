

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

            if ((listJson[mid])[attributeToCompare][0] > elementTarget):
                start = mid + 1
            else:
                end = mid

        return -1



