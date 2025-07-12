import json
import sqlite3


def search_using_and(query):
    print(f"\nBuscando por: '{query}' (busca OR implícita)")

    with sqlite3.connect("article.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            f'SELECT DISTINCT rank, id, titulo, texto, tags FROM artigos WHERE artigos MATCH "{query}" LIMIT 100'
        )
        return cursor.fetchall()


def search_using_near(query):
    print(f"\nBuscando por: '{query}' (palavras próximas)")
    with sqlite3.connect("article.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            f"""SELECT DISTINCT rank, id, titulo, texto, tags FROM artigos WHERE artigos MATCH 'NEAR(\"{query}\", 3)' LIMIT 100;"""
        )
        return cursor.fetchall()


def sarch_using_or(query):
    termo_busca_combinada = f"{query} OR clientes"
    print(f"\nBuscando por frase exata OU termo: '{termo_busca_combinada}'")
    with sqlite3.connect("article.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            f'SELECT DISTINCT rank, id, titulo, texto, tags FROM artigos WHERE artigos MATCH "{termo_busca_combinada}" LIMIT 100;'
        )
        return cursor.fetchall()


def setupdb():
    with sqlite3.connect("article.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS artigos USING fts5(id, titulo, texto, tags);
        """)

        conn.commit()

        with open("articles.json", "r") as f:
            articles = json.load(f)

        print("Total articles: ", len(articles))

        for article in articles:
            if article["titulo"].startswith("VÍDEO"):
                continue

            cursor.execute(
                """
                INSERT OR IGNORE INTO artigos (id, titulo, texto, tags)
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

    print("Database setup completed.")
