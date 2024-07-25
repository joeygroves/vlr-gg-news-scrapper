from bs4 import BeautifulSoup
import urllib.request

# Step 1: Define the URL and headers
url = "https://www.vlr.gg/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Step 2: Create a request object with the headers
request = urllib.request.Request(url, headers=headers)

# Step 3: Fetch the web page
response = urllib.request.urlopen(request)
web_content = response.read()

# Step 4: Parse the HTML content
soup = BeautifulSoup(web_content, 'html.parser')

# Step 5: Extract data
news_items = soup.find_all('div', class_='news-item-title text-of')

# Step 6: Iterate and print the extracted data
for item in news_items:
    title = item.text.strip()
    print(f"Title: {title}")

match_items = soup.find_all('a', class_='wf-module-item mod-match mod-color mod-bg-after-green')
for item in match_items:
    match_link = item.get('href')
    match_title = item.get_text(strip=True)
    print(f"Match Title: {match_title}")
    print(f"Link: https://www.vlr.gg{match_link}")
    print("-" * 20)