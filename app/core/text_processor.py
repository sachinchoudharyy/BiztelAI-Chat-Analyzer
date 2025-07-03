# # app/core/text_processor.py
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('wordnet')

# class TextProcessor:
#     def __init__(self):
#         self.stop_words = set(stopwords.words('english'))
#         self.lemmatizer = WordNetLemmatizer()

#     def preprocess(self, text: str) -> str:
#         text = re.sub(r'\W+', ' ', str(text).lower())
#         tokens = text.split()
#         tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
#         return " ".join(tokens)
# app/core/text_processor.py
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text: str) -> str:
        text = re.sub(r'\W+', ' ', str(text).lower())
        tokens = text.split()
        tokens = [self.lemmatizer.lemmatize(w) for w in tokens if w not in self.stop_words]
        return " ".join(tokens)

    def preprocess_dataframe(self, df, text_column='message'):
        df[text_column] = df[text_column].apply(self.preprocess_text)
        return df
