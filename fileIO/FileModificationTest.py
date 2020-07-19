import unittest
import os

from pathlib import Path


from fileIO.FileModification import FileModification


class FileModificationTest(unittest.TestCase):

    def test_head_append(self):
        fm = FileModification(os.path.join(Path(__file__).parent, "test.html"))
        fm.head_append('<script>')
        self.assertEqual('<head><script></head>', fm.content)
        fm.close()

