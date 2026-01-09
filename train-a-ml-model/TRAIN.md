```bash
pip install scikit-learn pandas nltk matplotlib
```



````
!wget -q https://github.com/mauricio-seiji/Dataset-news-articles-pt-br/a
!unzip -qq main.zip
!rm -rf news-articles
!mv Dataset-news-articles-pt-br-main news-articles
!rm -rf news-articles/__summarization__
!ls news-articles

dataset = load_files("news-articles"
, encoding="utf-8")
df = pd.DataFrame(dataset.data, columns=["text"])
df["label"] = pd.Categorical.from_codes(dataset.target, dataset.target_names)
df.head()

```

