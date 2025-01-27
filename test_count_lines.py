import unittest
from wc_tool import countlines,countbytes,countwords

class TestWcTool(unittest.TestCase):
    def test_emptyfile(self):
        self.assertEqual(countlines("zerolines.txt"),0)
        self.assertEqual(countbytes("zerolines.txt"),0)
        self.assertEqual(countwords("zerolines.txt"),0)


    def test_blankfile_with_newline(self):
        self.assertEqual(countlines("blank.txt"),1)
        self.assertEqual(countbytes("blank.txt"),1)
        self.assertEqual(countwords("blank.txt"),0)

    def test_nonemptyfile(self):
        self.assertEqual(countlines("test.txt"),7145)
        self.assertEqual(countbytes("test.txt"),342190)
        self.assertEqual(countwords("test.txt"),58164)#59792

    def test_nonexistencefile(self):
        self.assertFalse(countlines("abc.txt"))
        self.assertFalse(countbytes("abc.txt"))
        self.assertFalse(countwords("abc.txt"))


if __name__ == '__main__':
    unittest.main()