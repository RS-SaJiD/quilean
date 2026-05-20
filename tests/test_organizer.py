import unittest
from pathlib import Path
import tempfile
import shutil
from quilean.organizer import organize_files

class TestOrganizer(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        # Test files
        (self.test_dir / "image1.jpg").touch()
        (self.test_dir / "document.pdf").touch()
        (self.test_dir / "song.mp3").touch()
        (self.test_dir / "random.xyz").touch()
        (self.test_dir / "note.txt").touch()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_organize_files(self):
        organize_files(self.test_dir)
        
        self.assertTrue((self.test_dir / "Images").exists())
        self.assertTrue((self.test_dir / "Documents").exists())
        self.assertTrue((self.test_dir / "Audio").exists())
        self.assertTrue((self.test_dir / "Others").exists())

        self.assertTrue((self.test_dir / "Images" / "image1.jpg").exists())
        self.assertTrue((self.test_dir / "Others" / "random.xyz").exists())


if __name__ == '__main__':
    unittest.main()
