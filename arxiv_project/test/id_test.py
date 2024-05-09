import unittest
from unittest.mock import patch
from src.id_fetcher import IDFetcher

class TestIDFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = IDFetcher()

    @patch('requests.get')
    def test_fetch_ids(self, mock_get):
        # モックの設定
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<feed><entry><id>arXiv:1707.08567</id></entry><entry><id>arXiv:1609.04747</id></entry></feed>'
        
        # テスト実行
        result = self.fetcher.fetch_ids("machine learning", max_results=2)
        # 想定される結果を確認
        self.assertEqual(result, ['arXiv:1707.08567', 'arXiv:1609.04747'])

if __name__ == '__main__':
    unittest.main()
