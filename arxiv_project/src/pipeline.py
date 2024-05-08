from id_fetcher import IDFetcher
from article_fetcher import ArticleFetcher
from morphological_analyzer import MorphologicalAnalyzer
from database_manager import DatabaseManager

class ArxivPipeline:
    def __init__(self, base_url, db_path):
        self.id_fetcher = IDFetcher(base_url)
        self.article_fetcher = ArticleFetcher(base_url)
        self.analyzer = MorphologicalAnalyzer()
        self.db_manager = DatabaseManager(db_path)
    
    def run(self, query, max_results=10):
        # IDを取得
        paper_ids = self.id_fetcher.fetch_ids(query, max_results)
        
        for paper_id in paper_ids:
            # 各IDに対してabstractを取得
            abstract = self.article_fetcher.fetch_abstract(paper_id)
            
            # 形態素解析を実行
            analysis = self.analyzer.analyze(abstract)
            
            # 解析結果をデータベースに保存
            self.db_manager.save_analysis(paper_id, analysis)
        
        # データベース接続を閉じる
        self.db_manager.close()

    def close(self):
        self.db_manager.close()

if __name__ == '__main__':
    # ベースURLとデータベースのパスを設定
    base_url = "https://export.arxiv.org/api/query"
    db_path = "path/to/your/database.db"
    
    # パイプラインのインスタンス化と実行
    pipeline = ArxivPipeline(base_url, db_path)
    try:
        pipeline.run("machine learning", max_results=5)
    except Exception as e:
        print(f"Error running pipeline: {e}")
    finally:
        pipeline.close()
