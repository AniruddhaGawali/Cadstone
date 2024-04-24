import feedparser

def fetch_articles(url):
    feed = feedparser.parse(url)
    if feed.bozo:
        print("Error parsing feed:", feed.bozo_exception)
    else:
        articles = feed.entries
        return articles

def read_article(article):
    print(f"Title: {article.title}")
    print(f"Published Date: {article.published}")
    print("Summary:")
    print(article.summary)
    print("\n")

def main():
    url = 'https://indianexpress.com/section/india/'
    articles = fetch_articles(url)
    if articles:
        for idx, article in enumerate(articles, start=1):
            print(f"Article {idx}:")
            read_article(article)
    else:
        print("No articles found in the feed.")

if __name__ == '__main__':
    main()
