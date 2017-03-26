import Node
import ApiDrive
import DriveOp

def main():

    api = ApiDrive.ApiDrive()
    rootfs = api.getListFiles()
    if not rootfs:
        print('No files found.')
    else:
        print('Total Files:')
        print(len(rootfs))

    nodeRootFolder = Node.Node("application/vnd.google-apps.folder", 0, api.root, "rootDrive", -1)
    rootFolderSorted = sorted(rootfs,key=lambda parent : ('parents' not in parent, parent.get('parents', [])))
    op = DriveOp.DriveOp()
    l = []
    size = op.dfsDriveSize(rootFolderSorted, nodeRootFolder, l)
    print(size)

main()