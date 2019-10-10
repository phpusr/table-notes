#!/usr/bin/env python

import datetime
import os

"""
Production db backup script 
"""

now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
base_dir = os.path.dirname(os.path.abspath(__file__))
# json (default), xml, yaml (needs to install PyYAML)
dump_format = 'json'
file_name = f'prod_db_{now}.{dump_format}'
file_path = os.path.join(base_dir, file_name)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings_prod')
cmd = f'../manage.py dumpdata --indent=2 --format={dump_format} -o={file_path}'
os.system(cmd)

print(f'File saved to: {file_path}')
