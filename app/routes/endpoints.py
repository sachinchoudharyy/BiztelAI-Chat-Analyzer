# app/routes/endpoints.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd

from app.core.text_processor import TextProcessor
from app.core.sentiment_analyzer import SentimentAnalyzer
from app.core.article_matcher import ArticleMatcher


router = APIRouter()

# Mock placeholder for article prediction
def mock_article_link_prediction(text):
    return "https://www.washingtonpost.com/some-article"

# Request schema
class Message(BaseModel):
    chat_id: int
    agent: str
    message: str

from fastapi.responses import JSONResponse
from app.core.data_loader import DataLoader
from app.core.data_cleaner import DataCleaner

@router.get("/summary")
def get_dataset_summary():
    try:
        file_path = "data/BiztelAI_DS_Dataset_V1.csv"
        loader = DataLoader(file_path)
        df = loader.load_data()
        cleaner = DataCleaner(df)
        cleaned_df = cleaner.clean_data()

        summary = {
            "total_transcripts": cleaned_df['chat_id'].nunique(),
            "total_agents": cleaned_df['agent'].nunique(),
            "total_messages": len(cleaned_df),
            "avg_messages_per_transcript": round(cleaned_df.groupby('chat_id')['message'].count().mean(), 2),
            "top_agents_by_msg_count": cleaned_df['agent'].value_counts().head(3).to_dict()
        }

        return JSONResponse(content=summary)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/transform")
def transform_messages(messages: List[Message]):
    try:
        df = pd.DataFrame([msg.dict() for msg in messages])
        processor = TextProcessor()
        df['cleaned_message'] = df['message'].apply(processor.preprocess_text)
        return df[['chat_id', 'agent', 'cleaned_message']].to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze")
def analyze_transcript(messages: List[Message]):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([msg.dict() for msg in messages])

        # Preprocess text
        processor = TextProcessor()
        df['message'] = df['message'].apply(processor.preprocess_text)

        # Sentiment analysis
        analyzer = SentimentAnalyzer()
        sentiments = analyzer.get_agent_sentiment(df)

        # Count messages per agent
        agent_counts = df['agent'].value_counts().to_dict()

        # Combine all messages for article prediction (mocked)
        full_text = " ".join(df['message'].tolist())
        matcher = ArticleMatcher()
        best_article = matcher.find_best_match(full_text)
        article_link = best_article["link"]


        return {
            "possible_article_link": article_link,
            "agent_message_counts": agent_counts,
            "agent_sentiments": sentiments
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
