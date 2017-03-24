import Auth
import httplib2
import os
from apiclient import discovery

class ApiDrive:
    def __init__(self):
        auth = Auth.Auth('https://www.googleapis.com/auth/drive.metadata.readonly', 'client_secret.json', 'drive')
        credentials = auth.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.serviceV3 = discovery.build('drive', 'v3', http=http)
        self.serviceV2 = discovery.build('drive', 'v2', http=http)
        aboutDrive = self.serviceV2.about().get().execute()
        self.root = aboutDrive['rootFolderId']

    def getListFiles(self, gDriveService):
        res = gDriveService.files().list(q=" 'me' in owners or mimeType = 'application/vnd.google-apps.folder'",
                                         pageSize=1000,
                                         spaces="drive",
                                         fields="nextPageToken, files( id, name, size, mimeType, parents, quotaBytesUsed)").execute()
        resultList = res.get('files', [])
        nextTok = res.get('nextPageToken', None)
        while (nextTok != None):
            res = gDriveService.files().list(q=" 'me' in owners or mimeType = 'application/vnd.google-apps.folder'",
                                             pageSize=1000,
                                             spaces="drive",
                                             pageToken=nextTok,
                                             fields="nextPageToken, files( id, name, size, mimeType, parents, quotaBytesUsed)").execute()
            resulList = resulList + res.get('files', [])
            nextTok = res.get('nextPageToken', None)
