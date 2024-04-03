import os
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv
import time

load_dotenv()

class UploadFileToDrive:
    SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    APPLICATION_NAME = 'My Drive'
    
    def __init__(self, folder_name, file_path):
        self.folder_name = folder_name
        self.file_path = file_path

    @classmethod
    def service_account_file(cls):
        return cls.SERVICE_ACCOUNT_FILE

    @classmethod
    def application_name(cls):
        return cls.APPLICATION_NAME
    
    def get_authenticated_service(self):
        """Authenticates the user and returns the Drive service object."""
        scopes=['https://www.googleapis.com/auth/drive']

        # Load credentials from the service account JSON file
        credentials = service_account.Credentials.from_service_account_file(
            self.service_account_file(), scopes=scopes)

        # Build the Drive service object
        return build('drive', 'v3', credentials=credentials)

    def service(self):
        return self.get_authenticated_service()

    def get_folder_id(self):
        """Gets the ID of a folder with the given name."""
        try:
            results = self.service().files().list(
                q=f"name='{self.folder_name}' and mimeType='application/vnd.google-apps.folder'",
                pageSize=1,
                fields="files(id)"
            ).execute()
            files = results.get('files', [])
            if files:
                return files[0].get('id')
            else:
                print(f'Folder "{self.folder_name}" not found.')
                return None
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
    
    def upload_file(self):
        """Uploads a file to Google Drive."""
        try:
            file_metadata = {'name': os.path.basename(self.file_path)}
            folder_id = self.get_folder_id()

            if folder_id:
                file_metadata['parents'] = [folder_id]
            
            media = MediaFileUpload(self.file_path, resumable=True)
            start_time = time.time()  # Record start time
            uploaded_file = self.service().files().create(body=file_metadata, media_body=media, fields='id, webContentLink').execute()
            end_time = time.time()  # Record end time
            
            file_id = uploaded_file.get('id')

            # Set the file's sharing permissions to allow anyone with the link to view/download
            self.service().permissions().create(
                fileId=file_id,
                body={'role': 'reader', 'type': 'anyone'}
            ).execute()

            web_content_link = uploaded_file.get('webContentLink')

            if web_content_link:
                elapsed_time = end_time - start_time
                if elapsed_time > 5:
                    print(f"Warning: Upload took longer than 5 seconds: {elapsed_time} seconds")
                # print(f'File uploaded successfully. File ID: {file_id}')
                return f'Shareable or downloadable link: {web_content_link}. Time taken: {elapsed_time} seconds'
            else:
                print('An error occurred: Unable to retrieve shareable link.')
        except HttpError as error:
            print(f'An error occurred: {error}')


path_of_file_to_upload = 'C:/Users/user/Desktop/assembly_tutorial.pdf' #replace with the file path
folder_name_in_google_drive_to_upload_file_to = 'uploads'

upload_folder1 = UploadFileToDrive(
                    folder_name_in_google_drive_to_upload_file_to, 
                    path_of_file_to_upload
                    )

print(upload_folder1.upload_file())



