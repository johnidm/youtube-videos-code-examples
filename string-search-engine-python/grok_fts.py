import sqlite3
import json


def query(terms: str) -> list[dict]:
    with sqlite3.connect("article.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, titulo, rank FROM blog_fts WHERE blog_fts MATCH ? order by rank LIMIT 100""",
            (terms,),
        )
        return cursor.fetchall()


def setupdb():
    with sqlite3.connect("article.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS blog_fts")
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS blog_fts USING fts5(
                id,
                titulo,
                texto,
                tags,
                tokenize='porter' -- Use Porter stemmer for tokenization
            );
        """)

        with open("articles.json", "r") as f:
            articles = json.load(f)

        print("Total articles: ", len(articles))

        for article in articles:
            if article["titulo"].startswith("VÍDEO"):
                continue

            cursor.execute(
                """
                    INSERT OR IGNORE INTO blog_fts (id, titulo, texto, tags)
                    VALUES (?, ?, ?, ?)
                """,
                (
                    article["id"],
                    article["titulo"],
                    article["texto"],
                    article["tags"],
                ),
            )

        conn.commit()


if __name__ == "__main__":
    setupdb()
    rows = query("Suprimentos Contratos e Medições Contratos Tipos de Contratos")

    if not rows:
        print("No results found.")
    else:
        print(f"Total results: {len(rows)}")
        for row in rows:
            print(f"Score: {row[2]} - Title: {row[1]}")
