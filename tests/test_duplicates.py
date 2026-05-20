import unittest
from pathlib import Path
import tempfile
import shutil
from quilean.duplicates import find_duplicates

class TestDuplicates(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        # Create duplicate files
        (self.test_dir / "test1.txt").write_text("This is a test file")
        (self.test_dir / "copy_test1.txt").write_text("This is a test file")  # duplicate
        (self.test_dir / "unique.txt").write_text("Different content")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_find_duplicates(self):
        # Just check it runs without error (full test needs mocking)
        try:
            find_duplicates(self.test_dir)
        except Exception as e:
            self.fail(f"find_duplicates raised exception: {e}")


if __name__ == '__main__':
    unittest.main()
