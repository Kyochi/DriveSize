![alt tag](http://i.imgur.com/Q4CcJth.png)

Do you want to know the size of any folder in Google Drive ?  DriveSize is here.

## Installation & Usage setup

Before running DriveSize, your DriveSize directory should look like this:
>|-- drivesize/  
>|-- main.py  
>|-- client_secret.json  

### What is client_secret.json ?
It's a file containing your credentials to allow the script to get informations about your gDrive files.
### How to get my credentials ?
In a few steps (https://developers.google.com/drive/v3/web/quickstart/python):
> - Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
> - On the Add credentials to your project page, click the Cancel button.
>- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
>- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
>- Select the application type Other, enter the name "Drive API Quickstart", and click the Create button.
>- Click OK to dismiss the resulting dialog.
>- Click the file_download (Download JSON) button to the right of the client ID.
>- Move this file to your DriveSize directory and rename it client_secret.json

## Usage example
```shell
$ python main.py
Enter the name of the folder (regex) : Bahamas
"Bahamas 2017" Size: 20.0 Go
```
