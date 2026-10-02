"""Behavior checks that run without Streamlit or a live external service."""

import unittest

from reading_time import estimate_minutes


class ReadingTimeTests(unittest.TestCase):
    def test_empty_text_is_zero(self):
        self.assertEqual(estimate_minutes(""), 0)

    def test_whitespace_is_zero(self):
        self.assertEqual(estimate_minutes(" \n\t "), 0)

    def test_short_text_is_one_minute(self):
        self.assertEqual(estimate_minutes("A short article."), 1)

    def test_200_words_is_one_minute(self):
        self.assertEqual(estimate_minutes("word " * 200), 1)

    def test_201_words_rounds_up_to_two_minutes(self):
        self.assertEqual(estimate_minutes("word " * 201), 2)

    def test_400_words_is_two_minutes(self):
        self.assertEqual(estimate_minutes("word " * 400), 2)


if __name__ == "__main__":
    unittest.main()
