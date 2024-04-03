# Upload to Google Drive

## Overview

Upload to Google Drive is a Python script designed to simplify the process of uploading files to Google Drive. It leverages the Google Drive API to securely authenticate users and upload files to specified folders on Google Drive.

## Features

- **Simple File Upload**: Easily upload files to Google Drive with just a few lines of Python code.
- **Authentication Handling**: Automatically handles authentication with Google Drive using OAuth2 and service account credentials.
- **Flexible Configuration**: Allows users to specify the folder to upload files to on Google Drive.
- **Performance Monitoring**: Provides information about the time taken to upload files, with warnings for uploads that exceed a specified time limit.
- **Error Handling**: Robust error handling ensures smooth execution and provides detailed error messages in case of failures.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/JoseMiracle/UPLOAD_TO_GOOGLE_DRIVE.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Configure the project by setting up a Google Cloud Platform project and obtaining the necessary credentials for accessing the Google Drive API.
2. Provide the path of the file to upload and the name of the folder in Google Drive to upload the file to.
3. Run the script to upload the file to Google Drive.

Example usage:

```python
from upload_to_google_drive import UploadFileToDrive

# Provide the path of the file to upload and the name of the folder in Google Drive
path_of_file_to_upload = '/path/to/local/file.txt'
folder_name_in_google_drive_to_upload_file_to = 'uploads'

# Initialize the uploader
uploader = UploadFileToDrive(folder_name_in_google_drive_to_upload_file_to, path_of_file_to_upload)

# Upload the file to Google Drive
print(uploader.upload_file())
```

## Project Structure

```
upload_to_google_drive/
├── upload_to_google_drive.py
├── __init__.py
├── README.md
├── requirements.txt
├── ...
```

- `upload_to_google_drive.py`: Main module containing the UploadFileToDrive class.
- `__init__.py`: Initialization file for the Python package.
- `requirements.txt`: List of project dependencies.

## Dependencies

- Python 3.x
- Required Python packages listed in `requirements.txt`
