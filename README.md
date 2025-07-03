
# BiztelAI Transcript Analyzer 🚀

This project is a modular, production-ready Python pipeline and REST API that:
- Cleans and preprocesses chat transcripts
- Analyzes agent behavior and sentiment
- Matches discussion to a probable Washington Post article
- Provides REST endpoints for real-time interaction

---

## 🔧 Tech Stack
- Python 3.10+
- FastAPI
- Pandas, NumPy, TextBlob, Scikit-learn
- Modular OOP architecture
- Swagger docs auto-generated

---

## 📁 Project Structure

```
biztel_project/
│
├── data/
│   └── BiztelAI_DS_Dataset_V1.csv
├── notebooks/
│   └── EDA_Insights.ipynb
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── endpoints.py
│   ├── core/
│   │   ├── data_loader.py
│   │   ├── data_cleaner.py
│   │   ├── text_processor.py
│   │   ├── sentiment_analyzer.py
│   │   └── article_matcher.py
├── requirements.txt
├── README.md
└── run.sh (optional)
```

---

## 🚀 API Endpoints

### 📍 `POST /analyze`
Analyze a single chat transcript:
- Returns agent-wise sentiment
- Message counts
- Most likely article being discussed

### 📍 `POST /transform`
Preprocesses input messages using stopword removal, lemmatization, etc.

### 📍 `GET /summary`
Summarizes entire dataset: chat count, avg messages, top agents

---

## 🧪 How to Run Locally

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd biztel_project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API

```bash
uvicorn app.main:app --reload
```

Then open:  
📎 http://127.0.0.1:8000/docs

---

## 📊 EDA Notebook

Check `notebooks/EDA_Insights.ipynb` for visual insights:
- Agent activity
- Word clouds
- Chat patterns
- Sentiment distribution

---

## 📌 Assignment Goals Covered

- ✅ OOP data pipeline
- ✅ REST API via FastAPI
- ✅ Sentiment & summarization
- ✅ Article link prediction
- ✅ Modular, scalable design

---

## 🙌 Author

**Sachin Choudhary**  
Final Year B.Tech - AI & DS  
Open to AI/Data roles 🚀
