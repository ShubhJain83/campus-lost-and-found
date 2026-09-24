import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from matching import calculate_match_score, date_score
from validators import validate_date, validate_category


class TestProjectFunctions(unittest.TestCase):

    def setUp(self):
        self.lost = {
            "id": "L-TEST01",
            "type": "lost",
            "name": "Black Wallet",
            "category": "accessories",
            "description": "black leather wallet with card",
            "location": "Library",
            "date": "2026-09-20",
            "contact": "student@example.com",
            "status": "unresolved"
        }

        self.found = {
            "id": "F-TEST01",
            "type": "found",
            "name": "Black Wallet",
            "category": "accessories",
            "description": "black leather wallet",
            "location": "Library",
            "date": "2026-09-20",
            "contact": "finder@example.com",
            "status": "unresolved"
        }

    def test_exact_match_score(self):
        self.assertEqual(
            calculate_match_score(self.lost, self.found),
            100
        )

    def test_date_score(self):
        self.assertEqual(
            date_score("2026-09-20", "2026-09-20"),
            10
        )

        self.assertEqual(
            date_score("2026-09-20", "2026-09-22"),
            8
        )

    def test_date_validation(self):
        self.assertEqual(
            validate_date("2026-09-20"),
            "2026-09-20"
        )

        with self.assertRaises(ValueError):
            validate_date("20-09-2026")

    def test_category_validation(self):
        self.assertEqual(
            validate_category("electronics"),
            "electronics"
        )

        with self.assertRaises(ValueError):
            validate_category("invalid-category")


if __name__ == "__main__":
    unittest.main()
