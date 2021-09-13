from bs4 import BeautifulSoup as BS
import requests




# """save the contents of soup.title into match variable"""
# match = soup.title
# print(match)
# """print only the text minus the <title tag>"""
# print(match.text)
# """print the first div in the html file"""
# print(soup.div)
# """print the div with the footer class"""
# """classes use _"""
# print(soup.find('div',class_='footer'))
# """Print div article class"""
# article =soup.find('div',class_='article')
# print(article)
# """Print text from article anchor tag h2"""
# print(article.h2.a.text)
# """Print article summary"""
# summary  = article.p.text
# print(summary)
# """Find and Print all headlines and article summarys"""
# for article in soup.find_all('div',class_='article'):
#     headline = article.h2.a.text
#     print(headline)
#
#     summary = article.p.text
#     print(summary)
#     print()

"""Download info from Coreys Website"""

source = requests.get('http://coreyms.com').text

soup = BS(source, 'lxml')

# print(soup.prettify())

# """Get article info"""

# article = soup.find('article')
# print(article.prettify())
# headline = article.h2.a.text
# print(headline)

# """Get video info from article"""

# vid_src = article.find('iframe', class_='youtube-player')['src']
# # print(vid_src)

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# # print(vid_id)

# """Create Link from vid_id parsed above"""
# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)

"""Use for loop to find all articles and parse youtube links"""
for article in soup.find_all('article'):

"""Add Try Except clause to check for none value which will break script"""
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        
        """Create Link from vid_id parsed above"""
        yt_link = f'https://youtube.com/watch?v={vid_id}'
        print(yt_link)
    
    except Exception as e:
        yt_link = None

