# -*-coding:Utf-8 -*


class FileModification:

    def __init__(self, file_path):
        self._file_path = file_path
        file = open(self._file_path, "r")
        self.content = file.read()
        file.close()

    def head_append(self, newline):
        try:
            index = self.content.index('</head>')
            self.content = self.content[0:index] + newline + self.content[index:]

        except:
            print("Could not find index at file " + self._file_path)

    def write(self):
        file = open(self._file_path, "w")
        file.write(self.content)
        file.close()
