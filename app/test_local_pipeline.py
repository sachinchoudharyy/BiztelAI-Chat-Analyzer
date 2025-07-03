# app/main.py
from core.data_loader import DataLoader
from core.data_cleaner import DataCleaner
from core.text_processor import TextProcessor
from core.sentiment_analyzer import SentimentAnalyzer

if __name__ == "__main__":
    file_path = "data/BiztelAI_DS_Dataset_V1.csv"

    # Step 1: Load + Clean
    loader = DataLoader(file_path)
    df = loader.load_data()
    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_data()

    # Step 2: Preprocess Text
    processor = TextProcessor()
    processed_df = processor.preprocess_dataframe(cleaned_df)

    # Step 3: Sentiment Analysis
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.get_agent_sentiment(processed_df)

    print("💬 Agent Sentiments:")
    for agent, score in sentiment.items():
        sentiment_type = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
        print(f"  - {agent}: {sentiment_type} ({score:.2f})")