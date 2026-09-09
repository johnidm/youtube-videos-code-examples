import feedparser


def main():
    data = feedparser.parse('https://medium.com/feed/@johnidouglasmarangon')
    items = data["items"]

    posts = [
        {"title": i["title"], "publishedAt": i["published"], "link": i["link"]}
        for i in items
    ]

    print(posts)

if __name__ == "__main__":
    main()
