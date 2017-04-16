
from __future__ import print_function
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

class Auth:

    def __init__(self, scopes, secretFile, applicationName, credentialWindowsFile = 'mydrive.json'):
        self.uriScope = scopes
        self.clientSecretFile = secretFile
        self.appName = applicationName
        self.credentialWinFile = credentialWindowsFile


    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)

        credential_path = os.path.join(credential_dir, self.credentialWinFile)
        if not os.path.exists(credential_path):
            fileCred = open(credential_path, 'w')
            fileCred.close()

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.clientSecretFile, self.uriScope)
            flow.user_agent = self.appName
            credentials = tools.run_flow(flow, store)

        return credentials


