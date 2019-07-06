#!/usr/bin/env python

import datetime
import os

"""
Production db backup script 
"""

now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = f'prod_db_{now}'
file_path = os.path.join(base_dir, file_name)

cmd = f'../manage.py dumpdata --indent=2 > {file_path}.json'

os.system(cmd)

print(f'File saved to: {file_path}')
