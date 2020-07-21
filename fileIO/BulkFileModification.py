import glob

from FileModification import FileModification


class BulkFileModification:

    def __init__(self, path, extension):
        self._path = path
        self._extension = extension
        self.file_paths = self.get_file_paths()

    def bulk_head_insert(self, content):
        for file in self.file_paths:
            modifier = FileModification(file)
            modifier.head_append(content)
            modifier.write()
            
    def get_file_paths(self):
        return glob.glob(self._path + '**/*.' + self._extension, recursive=True)
