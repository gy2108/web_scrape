from bs4 import BeautifulSoup
import requests, csv

source = requests.get('http://coreyms.com').text

csv_file = opne('scrape_csv.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','youtube link'])

soup = BeautifulSoup(source, 'html.parser')
for article in soup.find_all('article'):
    heading = article.a.text
    print(heading)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_='youtube-palyer')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        youtbe_link = 'https://youtube.com/watch?v='+vid_id
    except Exception as e:
        youtbe_link = None
    print(youtbe_link)

    csv_writer.writerow([heading,summary,youtbe_link])