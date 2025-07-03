# app/core/article_matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ArticleMatcher:
    def __init__(self):
        # Simulated list of articles
        self.articles = [
            {
                "title": "Biden signs climate change bill into law",
                "link": "https://www.washingtonpost.com/climate-bill"
            },
            {
                "title": "Supreme Court overturns landmark ruling",
                "link": "https://www.washingtonpost.com/supreme-court"
            },
            {
                "title": "NASA reveals new images from James Webb telescope",
                "link": "https://www.washingtonpost.com/nasa-images"
            },
            {
                "title": "Ukraine conflict enters critical phase",
                "link": "https://www.washingtonpost.com/ukraine"
            }
        ]
        self.titles = [a["title"] for a in self.articles]
        self.vectorizer = TfidfVectorizer()

    def find_best_match(self, chat_text):
        all_docs = self.titles + [chat_text]
        tfidf_matrix = self.vectorizer.fit_transform(all_docs)
        similarity = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1])
        best_idx = similarity.argmax()
        return self.articles[best_idx]
