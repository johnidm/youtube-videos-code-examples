

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