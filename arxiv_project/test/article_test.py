import unittest
from src.article_fetcher import ArticleFetcher

class TestArticleFetcher(unittest.TestCase):
    def test_fetch_by_id(self):
        fetcher = ArticleFetcher()
        result = fetcher.fetch_by_id("1707.08567")
        self.assertIn("<summary>", result)

if __name__ == '__main__':
    unittest.main()

