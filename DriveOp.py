

class DriveOp:

    @staticmethod
    def getMoUsed(bytesUsed):
        return int(bytesUsed)/1024/1024

    @staticmethod
    def binarySearch(collection, target):
        start = 0
        end = len(collection)-1
        while (start < end):
            mid = collection[(start+end)/2]
            if (collection[mid] == target):
                return mid

            if (collection[mid] > target):
                start = mid + 1
            else:
                end = mid

        return -1
