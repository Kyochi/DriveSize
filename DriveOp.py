import Auth
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
class DriveManip:
    @staticmethod
    def getMoUsed(bytesUsed):
        return int(bytesUsed)/1024/1024

def main():
    auth = Auth.Auth('https://www.googleapis.com/auth/drive.metadata.readonly', 'client_secret.json', 'drive')
    credentials = auth.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(q="'me' in owners and  mimeType contains 'application/vnd.google-apps.folder'",
        pageSize=1000,
        spaces="drive",
        fields="files(id, name, size, mimeType, quotaBytesUsed)").execute()

#0BwjaEAUUi370ZVBKNXFheFRCWUE
    child = service.files().list(q="'0BwjaEAUUi370QWdEeWY2eTR6YjQ' in parents and 'me' in owners",
                                 fields="files(id, name, size, mimeType, quotaBytesUsed)", pageSize=1000).execute()
    childrens = child.get('files', [])
    for itm in childrens:
        print(itm)

    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        print(len(items))
        s = 0

main()