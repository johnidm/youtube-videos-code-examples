

## Algorithm Strategies

#### Full-Text Search (FTS5) in SQLite

SQLite has built-in support for full-text indexing via FTS5, which allows:

- Word-based tokenization
- Phrase matching
- Ranking based on match relevance
- Fast lookup via virtual tables

📌 Limitations: It doesn't support fuzzy/typo matching by default.

✅ Best for: Phrase/keyword searches where terms are known and relatively exact.

### Resources

- https://www.sqlitetutorial.net/sqlite-full-text-search/


#### Recomendação Combinada:

Para alta acurácia e eficiência, a melhor abordagem provavelmente será uma combinação de técnicas:

1. Utilize o FTS5 do SQLite para a pré-filtragem e ranqueamento inicial. Isso aproveitará a otimização do banco de dados para busca de texto completo.

2. No Python, refine os resultados do FTS5 usando algoritmos de similaridade. Aplique a Distância de Levenshtein ou Similaridade de Jaccard nos títulos, textos e palavras-chave dos resultados mais promissores do FTS5 para ranquear as correspondências com mais precisão. Isso é especialmente útil para capturar erros de digitação sutis que o FTS5 pode não priorizar da mesma forma.

Ao combinar o poder do FTS5 do SQLite com algoritmos de similaridade em Python, você pode criar um sistema de busca robusto e altamente preciso para o seu blog.

Combine this with a basic SQL query to first retrieve candidates (LIMIT 100), then rank with fuzzy logic.


```
# SQL: Get 100 candidates
SELECT id, title, text, keywords 
FROM blog_fts 
WHERE blog_fts MATCH 'clients accounts payable'
LIMIT 100;

# Python: Fuzzy re-ranking
fuzzy_search("Clients Accounts Payable", result_from_sql)
```

#### Enhancements:

- Apply stemming (via FTS5’s porter tokenizer or NLTK) to match word variations.
- Use TF-IDF for custom weighting (e.g., prioritize title matches).
- Add semantic search with sentence-transformers for queries where meaning matters more than exact matches (e.g., "client payment" matching "accounts payable").

#### Query Processing:

- Normalize the query (lowercase, stem).
- Support phrase queries ("Clients Accounts Payable") and loose term queries (Clients Accounts Payable).
- Combine results from FTS5 and TF-IDF/semantic search for hybrid ranking if needed.

#### Example Workflow for "Clients Accounts Payable"

1. Query Input: User enters "Clients Accounts Payable."
2. Preprocess: Stem to "client account payabl" (if using NLTK or FTS5 porter).
3. FTS5 Search: Query the FTS5 table with MATCH '"client account payabl"' or client AND account AND payabl.
4. Rank Results: Use BM25 scores from FTS5, optionally boosted by TF-IDF or semantic similarity.
5. Return Results: Display titles, snippets, and relevance scores.

#### Boost Fields: 

Yes, you can use fuzzy scoring to enhance your blog's search engine, especially for handling misspellings, partial matches, or variations in the query "Clients Accounts Payable." Fuzzy scoring, often implemented using algorithms like Levenshtein distance or trigram similarity, measures how similar two strings are, which is useful for matching terms despite typos or slight differences (e.g., "payble" vs. "payable"). Since you’re using Python and SQLite, fuzzy scoring can complement SQLite’s FTS5 full-text search by improving tolerance for imperfect queries.

###### Implementation Strategy

1. Primary Search with FTS5: Use SQLite FTS5 for efficient full-text search and ranking (using BM25).
2. Fuzzy Scoring: Apply fuzzy matching to filter or re-rank FTS5 results, or as a fallback for queries with no exact matches.
3. Fields: Apply fuzzy scoring to titles, content, and keywords, with higher weight to title matches.
4. Threshold: Set a similarity threshold (e.g., 80%) to balance precision and recall.