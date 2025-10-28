import requests
from bs4 import BeautifulSoup

# HTMLを取得して解析する関数
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードがエラーなら例外を出す
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# h1, h2, h3タグの見出しを抽出する関数
def extract_headlines(soup):
    if soup is None:
        return []
    headlines = []
    for tag in ['h1', 'h2', 'h3']:
        for element in soup.find_all(tag):
            headlines.append(element.get_text(strip=True))
    return headlines

# 実行例
url = "https://www.mof.go.jp/tax_policy/summary/consumption/d04.htm"
soup = fetch_html(url)
headlines = extract_headlines(soup)

print("Extracted Headlines:")
for headline in headlines:
    print("-", headline)