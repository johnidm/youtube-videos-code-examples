from rapidfuzz import fuzz  # pip install rapidfuzz


def fuzzy_search(query, rows):
    scored = []

    for row in rows:
        combined_text = f"{row['titulo']} {row['texto']} {row['tags']}"
        score = fuzz.token_sort_ratio(query, combined_text)
        scored.append((score, row))

    results = sorted(scored, key=lambda x: x[0], reverse=True)[:10]

    for score, post in results:
        print(f"Score: {score:.2f}, Título: {post['titulo']}")
