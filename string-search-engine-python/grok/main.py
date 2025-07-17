import sqlite3
from rapidfuzz import fuzz, process
import nltk
from nltk.stem.porter import PorterStemmer

# Initialize NLTK stemmer
nltk.download('punkt', quiet=True)
stemmer = PorterStemmer()

# Connect to SQLite database
conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

# Create FTS5 table if not exists
cursor.execute('''
    CREATE VIRTUAL TABLE IF NOT EXISTS blog_fts USING fts5(
        title, content, keywords,
        tokenize='porter'
    );
''')

# Insert sample data
sample_data = [
    (
        "Managing Client Accounts",
        "Best practices for handling accounts payable and receivable for clients.",
        "clients, accounts payable, accounts receivable, finance"
    ),
    (
        "Accounts Payable Guide",
        "Tips for managing accounts payable for small businesses.",
        "accounts payable, clients, business"
    ),
    (
        "General Finance Tips",
        "Overview of financial strategies for businesses.",
        "finance, business"
    )
]

cursor.executemany('''
    INSERT INTO blog_fts (title, content, keywords)
    VALUES (?, ?, ?)
''', sample_data)
conn.commit()

def preprocess_text(text):
    """Stem and lowercase text for consistent matching."""
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join(stemmer.stem(token) for token in tokens)

def search_blog(query, similarity_threshold=80, title_boost=2.0, title_weight=0.5):
    """
    Search blog with title boosting.
    Parameters:
    - similarity_threshold: Minimum fuzzy score for matches.
    - title_boost: Multiplier for FTS5 score if title contains query terms.
    - title_weight: Weight for title in fuzzy scoring (0 to 1).
    """
    # Preprocess query
    processed_query = preprocess_text(query)
    query_terms = processed_query.split()
    
    # FTS5 search
    fts_query = f'" {processed_query} "'  # Phrase query with stemmed terms
    cursor.execute('''
        SELECT title, content, keywords, rank
        FROM blog_fts
        WHERE blog_fts MATCH ?
        ORDER BY rank
    ''', (fts_query,))
    fts_results = cursor.fetchall()
    
    # Initialize results
    final_results = []
    
    if fts_results:
        for row in fts_results:
            title, content, keywords, fts_rank = row
            # Combine fields for fuzzy matching
            combined_text = f"{title} {content} {keywords}"
            # Compute fuzzy score for combined text
            fuzzy_score = fuzz.token_sort_ratio(query, combined_text)
            
            if fuzzy_score >= similarity_threshold:
                # Compute field-specific fuzzy scores
                title_score = fuzz.token_sort_ratio(query, title)
                content_score = fuzz.token_sort_ratio(query, content)
                keywords_score = fuzz.token_sort_ratio(query, keywords)
                
                # Weighted fuzzy score (title gets higher weight)
                weighted_fuzzy = (
                    title_weight * title_score +
                    (1 - title_weight) * 0.5 * (content_score + keywords_score)
                )
                
                # Boost FTS5 score if query terms appear in title
                title_lower = title.lower()
                title_match = any(term in title_lower for term in query_terms)
                boosted_fts_rank = fts_rank * title_boost if title_match else fts_rank
                
                # Combine FTS5 and fuzzy scores
                combined_score = weighted_fuzzy * 0.6 + (-boosted_fts_rank) * 0.4
                
                final_results.append({
                    'title': title,
                    'content': content[:100] + '...',
                    'keywords': keywords,
                    'score': combined_score
                })
    
    # Fallback: If no FTS5 results, try fuzzy matching on all documents
    if not final_results:
        cursor.execute('SELECT title, content, keywords FROM blog_fts')
        all_docs = cursor.fetchall()
        for title, content, keywords in all_docs:
            combined_text = f"{title} {content} {keywords}"
            fuzzy_score = fuzz.token_sort_ratio(query, combined_text)
            
            if fuzzy_score >= similarity_threshold:
                # Compute field-specific fuzzy scores
                title_score = fuzz.token_sort_ratio(query, title)
                content_score = fuzz.token_sort_ratio(query, content)
                keywords_score = fuzz.token_sort_ratio(query, keywords)
                
                # Weighted fuzzy score
                weighted_fuzzy = (
                    title_weight * title_score +
                    (1 - title_weight) * 0.5 * (content_score + keywords_score)
                )
                
                final_results.append({
                    'title': title,
                    'content': content[:100] + '...',
                    'keywords': keywords,
                    'score': weighted_fuzzy
                })
    
    # Sort by combined score
    final_results.sort(key=lambda x: x['score'], reverse=True)
    return final_results

# Example usage
query = "Clients Accounts Payble"  # Note the misspelling
results = search_blog(query, title_boost=2.0, title_weight=0.5)

# Display results
for result in results:
    print(f"Title: {result['title']}")
    print(f"Content: {result['content']}")
    print(f"Keywords: {result['keywords']}")
    print(f"Score: {result['score']:.2f}\n")

# Close connection
conn.close()