from bs4.element import PageElement
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get url of page
def get_url(page_num: int):
  return 'https://2ch.hk/b/arch/' + str(page_num) + '.html'

# Get HTML of page
def get_html(url: str):
    page = requests.get(url)
    return page.content

# Check if element is not line break
def check_not_line_break(el: PageElement):
  if el == '\n':
    return False
  return True

# Check if element is thread link
def check_is_thread_link(el: PageElement):
  if isinstance(el, str):
    return False
  if el.attrs.get('href') is not None:
    return True
  return False

# Get pages coung
def get_pages_count(html: bytes):
  soup = BeautifulSoup(html, "html.parser")
  pagerEl = soup.find(class_="pager_arch")
  pagesEls = list(filter(check_not_line_break, pagerEl.contents))
  count = len(pagesEls) - 1
  return count

# Get threads html list element
def get_threads_html_list(html: bytes):
  soup = BeautifulSoup(html, "html.parser")
  threadsContainerEl = soup.find(class_="box__data")
  return threadsContainerEl.children

# Get threads from page
def get_threads(html_nodes: list[PageElement]):
  threads = []
  for el in html_nodes:
    if not check_is_thread_link(el):
      continue
    
    link = el.attrs['href']
    id = get_thread_id_from_link(link)
    date = get_date_from_thread_link(link)
    title = el.text
    thread = { 'title': title, 'link': link, 'date': date, 'id': id }
    threads.append(thread)

  return threads

def get_thread_id_from_link(link: str):
  return link.split('/')[-1].split('.')[0]

def get_date_from_thread_link(link: str):
  return link.split('/')[-3]

pages_count_start = 0
url = get_url(pages_count_start)
html = get_html(url)
pages_count = get_pages_count(html)

for page_num in range(pages_count_start, pages_count + 1):
  url = get_url(page_num)  
  html = get_html(url)
  threads = get_threads(get_threads_html_list(html))
  df = pd.DataFrame(threads, columns=['id', 'date', 'title', 'link'])
  df.to_csv(
    path_or_buf='dataset_id-date-title-link.csv',
    columns=['id', 'date', 'title', 'link'],
    index=False,
    mode='a'
  )
  print(f'page {page_num} of {pages_count}')

