import Auth
import httplib2
import os
from apiclient import discovery

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


    rootfile = service.files().list(q=" 'me' in owners and 'root' in parents ",
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

    for itemSorted in rootFolderSorted:
        print(itemSorted)

main()