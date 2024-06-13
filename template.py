import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    'src/__init__.py',
    'src/prompt.py',
    'src/helper.py',
    '.env',
    'setup.py',
    'research/trails.ipynb',
    'app.py',
    'store_index.py',
    'static/.gitkeep',
    'templates/chat.html'
]

for file in list_of_files:
    file = Path(file)
    file_dir, file_name = os.path.split(file)

    if(file_dir):
        os.makedirs(file_dir, exist_ok = True)
        logging.info(f'Created directory: {file_dir} for the file {file_name}')

    if(not os.path.exists(file) or (os.path.getsize(file) == 0)):
        with open(file, 'w') as f:
            pass
            logging.info(f'Created empty file: {file}')

    else:
        logging.info(f'File already exists: {file}')   