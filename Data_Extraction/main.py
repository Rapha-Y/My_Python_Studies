import requests
import json
from bs4 import BeautifulSoup

res = requests.get('https://serenesforest.net')
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

pageLink = soup.find(class_="more_posts")
hrefTag = pageLink.find('a')

prev_page = []
page = requests.get(hrefTag.get('href'))
prev_page.append(BeautifulSoup(page.text, 'html.parser'))

all_post = []

posts = prev_page[0]
posts = posts.find_all(class_="post")
for post in posts:
    title = post.find('h2').text
    author = post.find(class_="meta-author").text    
    full_preview = post.find(class_="entry")

    for tag in full_preview.find_all('a'):
        tag.replace_with('')
    preview = full_preview.text
    
    all_post.append({
        'title': title,
        'author': author,
        'preview': preview
    })    

with open('posts.json', 'w') as json_file:
    json.dump(all_post, json_file, indent=3, ensure_ascii=False)