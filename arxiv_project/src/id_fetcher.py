import requests
from bs4 import BeautifulSoup

class IDFetcher:
    def __init__(self, base_url="https://export.arxiv.org/api/query"):
        self.base_url = base_url

    def fetch_by_id(self, query, max_results=10):
        url = f"{self.base_url}?search_query={query}&start=0&max_results={max_results}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'xml')
            return [entry.id.text.strip() for entry in soup.find_all('entry')]
        else:
            raise Exception("Failed to fetch data from arXiv")
