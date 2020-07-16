import unittest

from fileIO.FileModification import FileModification


class FileModificationTest(unittest.TestCase):

    def test_head_append(self):
        fm = FileModification("test.html")
        fm.head_append('<script>')
        self.assertEqual('<head><script></head>', fm.content)

