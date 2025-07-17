import nltk
from nltk.stem.porter import PorterStemmer

nltk.download("punkt")
nltk.download("punkt_tab")


stemmer = PorterStemmer()


def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    return " ".join(stemmer.stem(token) for token in tokens)


query = preprocess_text("Suprimentos Contratos e Medições Contratos Tipos de Contratos")
print(query)
