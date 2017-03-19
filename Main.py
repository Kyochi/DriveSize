import Auth
import httplib2
import os
from apiclient import discovery

from DriveOp import *
import Node


def main():
    auth = Auth.Auth('https://www.googleapis.com/auth/drive.metadata.readonly', 'client_secret.json', 'drive')
    credentials = auth.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    service2 = discovery.build('drive', 'v2', http=http)

    aboutDrive = service2.about().get().execute()
    rootid = aboutDrive['rootFolderId']
    print(rootid)

    results = service.files().list(q="'me' in owners and  not mimeType contains 'application/vnd.google-apps'",
        pageSize=1000,
        spaces="drive",
        fields="files(id, name, size, mimeType, quotaBytesUsed)").execute()


    rootfile = service.files().list(q=" 'me' in owners",
        pageSize=1000,
        spaces="drive",
        fields="files(id, name, size, mimeType, parents, quotaBytesUsed)").execute()


    rootfs = rootfile.get('files', [])
    rootFolderSorted = sorted(rootfs,key=lambda parent : parent['parents'][0])

    if not rootfs:
        print('No files found.')
    else:
        print('Total Files:')
        print(len(rootfs))

    nodeRootFolder = Node.Node("application/vnd.google-apps.folder", 0, rootid, "rootDrive", -1)

    i = 0
    n = 0
    for itemSorted in rootFolderSorted:
        print(itemSorted)
        if (not(itemSorted['mimeType'].startswith("application/vnd.google-apps"))):
            i = i + float(itemSorted['size'])
            n = n+1

    print(i)
    print(n)

    op = DriveOp()
    size = op.dfsDriveSize(rootFolderSorted, nodeRootFolder)
    print(len(rootFolderSorted))
    print(size)
    print(op.getMo(size))

main()