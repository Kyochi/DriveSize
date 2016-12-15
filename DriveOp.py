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

    results = service.files().list(q="'me' in owners and not mimeType contains 'application/vnd.google-apps'",
        pageSize=1000,
        spaces="drive",
        fields="files(id, name, size, mimeType, quotaBytesUsed)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        print(len(items))
        s = 0
        for item in items:
            s += DriveManip.getMoUsed(item["quotaBytesUsed"])#(int(item["quotaBytesUsed"])/1024)/1024
            if ((int(item["quotaBytesUsed"])/1024)/1024 > 100):
                print(item)

        print(s)

main()