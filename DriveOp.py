

class DriveOp:

    @staticmethod
    def getMoUsed(bytesUsed):
        return int(bytesUsed)/1024/1024

    @staticmethod
    def jsonBinarySearch(listJson, attributeToCompare, elementTarget):
        start = 0
        end = len(listJson)-1
        while (start < end):
            mid = listJson[(start+end)/2]
            if (listJson[mid][attributeToCompare][0] == target):
                return mid

            if (listJson[mid][attributeToCompare][0] > target):
                start = mid + 1
            else:
                end = mid

        return -1





