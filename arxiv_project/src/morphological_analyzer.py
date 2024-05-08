import MeCab

class MorphologicalAnalyzer:
    def __init__(self):
        self.analyzer = MeCab.Tagger()

    def analyze(self, text):
        return self.analyzer.parse(text)
