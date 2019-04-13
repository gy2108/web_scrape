from bs4 import BeautifulSoup
import requests, csv

#Dail news Headline and Summary from inshorts.com
source = requests.get('https://inshorts.com/en/read').text
with open('DailyNews_csv.csv' , 'w', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline','summary','ServerProblem'])

    soup = BeautifulSoup(source, 'html.parser')

    for article in soup.find_all('div',{'class':'news-card z-depth-1'}):
        try:
            server_problem = ''
            heading = article.a.span.text
            # print(heading)
            summary = article.find('div', itemprop='articleBody').text
            # print(summary)
        except Exception as e:
            server_problem = "Some Error Occured while fetching the NEWS!!"
        csv_writer.writerow([heading,summary,server_problem])

#Python articles from coreyms.com
source = requests.get('http://coreyms.com').text

csv_file = open('scrape_csv.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','youtube link'])

soup = BeautifulSoup(source, 'html.parser')
for article in soup.find_all('article'):
    heading = article.a.text
    # print(heading)
    summary = article.find('div', class_='entry-content').p.text
    # print(summary)
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        youtbe_link = 'https://youtube.com/watch?v='+vid_id
    except Exception as e:
        youtbe_link = None
    # print(youtbe_link)

    csv_writer.writerow([heading,summary,youtbe_link])