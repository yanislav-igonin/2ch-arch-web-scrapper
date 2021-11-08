import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_url(page_num):
  return 'https://2ch.hk/b/arch/' + str(page_num) + '.html'

def get_html(url):
    page = requests.get(url)
    return page.content

def check_not_line_break(el):
  if el == '\n':
    return False
  return True

def check_is_thread_link(el):
  if isinstance(el, str):
    return False
  if el.attrs.get('href') is not None:
    return True
  return False

def get_pages_count(html):
  soup = BeautifulSoup(html, "html.parser")
  pagerEl = soup.find(class_="pager_arch")
  pagesEls = list(filter(check_not_line_break, pagerEl.contents))
  count = len(pagesEls) - 1
  return count

def get_threads_html_list(html):
  soup = BeautifulSoup(html, "html.parser")
  threadsContainerEl = soup.find(class_="box-data")
  return threadsContainerEl.children

def get_threads(html_nodes):
  # threads = pd.DataFrame(columns=['title', 'link'])
  threads = []
  for el in html_nodes:
    if check_is_thread_link(el):
      thread = { 'title': el.text, 'link': el.attrs['href'] }
      # threads.append(thread, ignore_index=True)
      threads.append(thread)
  return threads


pages_count_start = 0
url = get_url(pages_count_start)
html = get_html(url)
pages_count = get_pages_count(html)

for page_num in range(pages_count_start, pages_count + 1):
  url = get_url(page_num)  
  html = get_html(url)
  threads = get_threads(get_threads_html_list(html))
  df = pd.DataFrame(threads, columns=['title', 'link'])
  df.to_csv(path_or_buf='dataset_links_and_titles.csv', columns=['title', 'link'], index=False, mode='a')
  print(f'page {page_num + 1} of {pages_count + 1}')

