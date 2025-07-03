# app/core/sentiment_analyzer.py
from textblob import TextBlob

class SentimentAnalyzer:
    def get_sentiment(self, text: str) -> float:
        """
        Returns sentiment polarity score in range [-1, 1]
        """
        return TextBlob(text).sentiment.polarity

    def get_agent_sentiment(self, df, agent_col='agent', text_col='message'):
        """
        Returns sentiment scores grouped by each agent
        """
        sentiment_scores = {}
        agents = df[agent_col].unique()

        for agent in agents:
            messages = df[df[agent_col] == agent][text_col].tolist()
            full_text = " ".join(messages)
            sentiment = self.get_sentiment(full_text)
            sentiment_scores[agent] = sentiment
        
        return sentiment_scores
