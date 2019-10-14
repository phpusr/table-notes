#!/usr/bin/env python

import datetime
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pprint import pprint


def backup_db_to_file():
    """
    Production db backup script
    """

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # json (default), xml, yaml (needs to install PyYAML)
    dump_format = 'json'
    file_name = f'prod_db_{now}.{dump_format}'
    file_path = f'/tmp/{file_name}'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.backup')
    cmd = f'../manage.py dumpdata --indent=2 --format={dump_format} -o={file_path}'
    os.system(cmd)

    print(f'File saved to: {file_path}')
    return file_path


class GoogleDrive:

    def __init__(self):
        scopes = ['https://www.googleapis.com/auth/drive']
        service_account_file = 'gdrive_account.json'
        credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
        self.service = build('drive', 'v3', credentials=credentials)

    def upload_file(self, file_path):
        folder_id = '1DyhiFFUgmpnwxunHT5yYbqJAw023kjeW'
        file_name = file_path[file_path.rfind('/') + 1:]
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        media = MediaFileUpload(file_path, resumable=True)
        result = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('File uploaded:', result)

    def print_available_files(self):
        result = self.service.files().list(pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
        pprint(result)


file_path = backup_db_to_file()

g_drive = GoogleDrive()
g_drive.upload_file(file_path)

os.remove(file_path)
