import requests
from bs4 import BeautifulSoup

class ArticleFetcher:
    def __init__(self, base_url="https://export.arxiv.org/api/query"):
        self.base_url = base_url
    
    def fetch_by_id(self, paper_id):
        # arXiv APIを使用して論文のデータを取得
        query = f"{self.base_url}?id_list={paper_id}"
        response = requests.get(query)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to fetch data from arXiv")
   
    def fetch_abstract(self, paper_id):
        # arXiv APIを使用して論文のデータを取得し、抄録を抽出
        xml_data = self.fetch_by_id(paper_id)
        return self.parse_abstract(xml_data)
    
    def parse_abstract(self, xml_data):
        # BeautifulSoupを使用して要約を抽出
        soup = BeautifulSoup(xml_data, 'xml')
        abstract = soup.find('summary').text.strip()
        return abstract

class PaperLoader:
    def __init__(self, fetcher):
        self.fetcher = fetcher
        self.papers = []
    
    def load_paper(self, paper_id):
        # 論文データを取得し、パースしてpapersリストに追加
        xml_data = self.fetcher.fetch_by_id(paper_id)
        abstract = self.fetcher.parse_abstract(xml_data)
        self.papers.append({"id": paper_id, "abstract": abstract})
    
    def get_papers(self):
        return self.papers
    
if __name__ == "__main__":
    # インスタンス化
    fetcher = ArticleFetcher()
    loader = PaperLoader(fetcher)

    paper_id = "1707.08567"
    loader.load_paper(paper_id)

    # 結果を表示
    papers = loader.get_papers()
    for paper in papers:
        print(f"Paper ID: {paper['id']}, Abstract: {paper['abstract']}")
