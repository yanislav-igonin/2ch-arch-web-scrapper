import requests
from bs4 import BeautifulSoup

def get_html(url):
    page = requests.get(url)
    return page.content

def check_not_line_break(el):
  if el == '\n':
    return False
  return True

def get_pages_count(html):
  soup = BeautifulSoup(html, "html.parser")
  pagerEl = soup.find(class_="pager_arch")
  pagesEls = list(filter(check_not_line_break, pagerEl.contents))
  count = len(pagesEls) - 1
  return count

pagesCountStart = 0
url = "https://2ch.hk/b/arch/" + pagesCountStart + ".html"
html = get_html(url)
pagesCount = get_pages_count(html)

