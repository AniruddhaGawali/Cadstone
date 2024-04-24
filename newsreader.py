import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from tempfile import NamedTemporaryFile
import playsound

def fetch_article(url):
    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        data = soup.find('article')
        title = data.find('h1').text if data.find('h1') else "Title Not Found"
        mainarticle = data.find('div', class_='crayons-article__main').text if data.find('div', class_='crayons-article__main') else "Summary Not Found"
        published = data.find('time')['datetime'] if data.find('time') and 'datetime' in data.find('time').attrs else "Date Not Found"

        return {
            'title': title,
            'summary': mainarticle,
            'published': published
        }
    else:
        print(f"Failed to fetch article: {res.status_code}")
        return None


def read_article(article):
    title = article['title']
    summary = article['summary']

    # Create audio file
    tts = gTTS(f"Title: {title}.\n\n {summary}", lang='en',tld='co.in')
    temp_file = NamedTemporaryFile(delete=True)
    tts.write_to_fp(temp_file)
    print(f"Reading article: {title}")

    # Play the audio using playsound
    playsound.playsound(temp_file.name, True)

def main():
    
    url = input("Enter the URL of the article: ")
    print(f"Loading article from {url}... \n\n\n")
    article = fetch_article(url)
    if article:
        read_article(article)
    else:
        print("No article found. or not permitted to access the article.")

if __name__ == '__main__':
    main()
