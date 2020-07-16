import glob


class BulkFileModification:

    def __init__(self, path, extension):
        self._path = path
        self._extension = extension
        self.file_paths = self.get_file_paths()

    def bulk_head_insert(self, content):
        pass

    def get_file_paths(self):
        return glob.glob(self._path + '**/*.' + self._extension, recursive=True)
