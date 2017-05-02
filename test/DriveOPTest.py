import unittest
from drivesize.DriveOp import DriveOp

class DriveOPTest(unittest.TestCase):

    def testGetGO(self):
        go = 13
        octet = 13958643712
        self.assertEqual(DriveOp.getGo(octet), go)



    if __name__ == '__main__':
            unittest.main()