import Node
import ApiDrive

def main():

    api = ApiDrive()

    results = api.serviceV3.files().list(q="'me' in owners and  not mimeType contains 'application/vnd.google-apps'",
        pageSize=1000,
        spaces="drive",
        fields="files(id, name, size, mimeType, quotaBytesUsed)").execute()


    rootfile = api.serviceV2.files().list(q=" 'me' in owners ",
        pageSize=1000,
        spaces="drive",
        fields="nextPageToken, files( id, name, size, mimeType, parents, quotaBytesUsed)").execute()


    rootfs = rootfile.get('files', [])

    if not rootfs:
        print('No files found.')
    else:
        print('Total Files:')
        print(len(rootfs))

    nodeRootFolder = Node.Node("application/vnd.google-apps.folder", 0, api.root, "rootDrive", -1)

    rootFolderSorted = sorted(rootfs,key=lambda parent : parent['parents'][0])

    # for itemSorted in rootFolderSorted:
    #     print(itemSorted)
    #     if (not(itemSorted['mimeType'].startswith("application/vnd.google-apps"))):
    #         i = i + float(itemSorted['size'])
    #         n = n+1
    #
    # print(i)
    # print(n)

    # op = DriveOp()
    # size = op.dfsDriveSize(rootFolderSorted, nodeRootFolder)
    # print(len(rootFolderSorted))
    # print(size)
    # print(op.getMo(size))

main()