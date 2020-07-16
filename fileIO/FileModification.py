# -*-coding:Utf-8 -*


class FileModification:

    def __init__(self, file_path):
        self._file_path = file_path
        self._file = open(self._file_path, "r")
        self.content = self._file.read()
        self._file.close()

    def head_append(self, newline):
        index = self.content.index('</head>')
        self.content = self.content[0:index] + newline + self.content[index:]

    def write(self):
        self._file = open(self._file_path, "w")
        self._file.write(self.content)
        self._file.close()
