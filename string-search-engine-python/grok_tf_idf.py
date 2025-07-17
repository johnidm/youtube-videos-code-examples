from sklearn.feature_extraction.text import TfidfVectorizer  # pip install scikit-learn
import numpy as np
import json


def vectorizer(query):
    with open("articles.json", "r") as f:
        articles = json.load(f)

    print("Total articles: ", len(articles))

    documents = [
        f"{article['titulo']} {article['texto']} {article['tags']}"
        for article in articles
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents + [query])
    cosine_similarities = (
        np.dot(tfidf_matrix[:-1], tfidf_matrix[-1].T).toarray().flatten()
    )

    ranked_docs = sorted(
        zip(documents, cosine_similarities), key=lambda x: x[1], reverse=True
    )
    for doc, score in ranked_docs:
        if score > 0:
            print(f"Document: {doc[:80]}\nScore: {score}\n")


if __name__ == "__main__":
    vectorizer("Suprimentos Contratos e Medições Contratos Tipos de Contratos")
