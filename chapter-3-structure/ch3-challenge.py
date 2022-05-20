# (c) Maximilian Schwarzmüller / Academind GmbH

from os import path, makedirs
from pathlib import Path


class DiskStorage:
    """ A class which allows us to create DiskStorage instances """
    def __init__(self, directory_name):
        self.storage_directory = directory_name

    def get_directory_path(self):
        return Path(self.storage_directory)

    def create_directory(self):
        if (not path.exists(self.get_directory_path())):
            makedirs(self.storage_directory)

    # Warning: Directory must exist in advance
    def insert_file(self, file_name, content):
        file_path = self.get_directory_path()
        file = open(file_path / file_name, 'w')
        file.write(content)
        file.close()
        # TODO: Add proper error handling


log_storage = DiskStorage('logs')

# log_storage.create_directory()
# if we commen-out th line above, the code will work properly
log_storage.insert_file('test.txt', 'Test')
