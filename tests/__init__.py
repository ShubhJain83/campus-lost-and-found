import unittest


class TestProject(unittest.TestCase):

    def test_basic_math(self):
        self.assertEqual(2 + 2, 4)

    def test_string_check(self):
        self.assertEqual("wallet".lower(), "wallet")


if __name__ == "__main__":
    unittest.main()