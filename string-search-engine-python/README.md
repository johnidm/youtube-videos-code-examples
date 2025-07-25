

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
- https://www.sqlite.org/fts5.html


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

## SQLite

### Ranking Results (BM25)

FTS5 includes a built-in ranking algorithm called BM25 (Best Match 25) to sort results by relevance. The BM25 function returns a real number representing the relevance score. Lower scores are more relevant.

```
SELECT title, content, bm25(documents) AS score
FROM documents
WHERE documents MATCH 'sqlite search'
ORDER BY score;
```

#### Ranking Customization (FTS5):

You can influence the BM25 ranking by providing custom weights for columns and even for specific phrases.

```
-- Example of custom column weights
CREATE VIRTUAL TABLE documents USING fts5(title, content, bm25(0.5, 1.0));
-- Here, 'content' (column index 1) has twice the weight of 'title' (column index 0)
```

More advanced customization involves creating your own ranking functions using the xRank callback (requires C-level integration).

### Custom Tokenizers

By default, FTS uses a simple tokenizer that splits text into words based on whitespace and punctuation. You can define custom tokenizers to handle specific linguistic requirements (e.g., Chinese, Japanese, or special characters).

```
-- Example (not runnable directly without C code for custom tokenizer)
CREATE VIRTUAL TABLE documents USING fts5(content, tokenize = 'my_custom_tokenizer');
```

#### How FTS Works Internally (Simplified):

Tokenization: When you insert text into an FTS table, it's first broken down into individual "tokens" (words) by a tokenizer.

Inverted Index: These tokens are then added to a special data structure called an "inverted index." An inverted index maps each unique token to the documents (or rows) and positions where it appears.

Example:

- "sqlite" -> Document 1 (positions: 3, 10), Document 3 (positions: 5)
- "tutorial" -> Document 1 (positions: 1), Document 2 (positions: 8)

Searching: When you execute a MATCH query, FTS uses the inverted index to quickly locate documents containing the specified terms. It then performs further processing (like phrase matching or proximity searches) on the identified documents.

Ranking: For relevance ranking, algorithms like BM25 consider factors like the frequency of terms in a document, the frequency of terms across all documents, and document length.

### Core Concept
SQLite’s FTS modules create virtual tables optimized for text search. Unlike regular SQLite tables, FTS tables index text content to enable fast keyword searches, similar to how a search engine indexes web pages. The key components are:

- Virtual Tables: FTS tables are created using the FTS3, FTS4, or FTS5 module. These tables store text data and an inverted index, which maps words (or tokens) to their locations in the table.

- Tokenization: Text is broken into tokens (usually words) using a tokenizer. For example, the sentence “The quick brown fox” might be tokenized into ["the", "quick", "brown", "fox"]. SQLite supports various tokenizers (e.g., simple, porter, unicode61) to handle different languages or stemming needs.

- Inverted Index: The FTS module maintains an index that maps each token to the rows and columns where it appears. This enables rapid lookup of documents containing specific words.

- Query Processing: FTS supports queries using the MATCH operator, which searches the index for tokens. It supports exact matches, phrase searches, prefix searches, and even complex queries with logical operators (e.g., AND, OR, NOT).

- Ranking: FTS5 includes built-in ranking functions (like bm25) to score results based on relevance, useful for sorting search results.