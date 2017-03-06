import Auth
import httplib2
import os
from apiclient import discovery

def main():
    auth = Auth.Auth('https://www.googleapis.com/auth/drive.metadata.readonly', 'client_secret.json', 'drive')
    credentials = auth.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(q="'me' in owners and  not mimeType contains 'application/vnd.google-apps'",
        pageSize=1000,
        spaces="drive",
        fields="files(id, name, size, mimeType, quotaBytesUsed)").execute()

#XXX pour choper les enfants d'un parents XXXX
    #child = service.files().list(q="'XXXX' in parents and 'me' in owners",
    #                             fields="files(id, name, size, mimeType, quotaBytesUsed)", pageSize=1000).execute()
   # childrens = child.get('files', [])

    rootfile = service.files().list(q=" 'me' in owners and 'root' in parents "
                                    , fields="files(id, name, size, mimeType, parents)").execute()


    items = results.get('files', [])
    rootfs = rootfile.get('files', [])
    print(len(rootfs))

    for rf in rootfs:
        print(rf['parents'][0])



    print("General files")

    if not items:
        print('No files found.')
    else:
        print('Files:')
        print(len(items))

main()