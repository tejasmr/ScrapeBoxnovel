import time
# from bs4 import BeautifulSoup
from tqdm import tqdm
from definitions import ID, NOVEL_URL, TAG_NAME, XPATH
from driver import driver
from logger import log
from scraper import collect_chapter_content

def get_chapter_count(url=""):
    driver.get(url)
    book_name = url.removeprefix(NOVEL_URL + "/").removesuffix("/")
    # with open(book_name + '.html', 'w', encoding='utf-8') as fp:
    #     fp.write(driver.page_source)
    time.sleep(2)
    elements = driver.find_elements(by= TAG_NAME, value='a')
    count = 0
    for element in elements:
        link = element.get_attribute('href')
        if link is None:
            continue
        if not book_name in link:
            continue
        if not '/chapter' in link:
            continue
        count += 1
    
    return count

def get_chapter_content_from_novel(url=""):
    count = get_chapter_count(url)
    # print(count)
    chapter_map = {}
    for i in range(1, count+1):
        chapter_map[i] = collect_chapter_content(url + '/chapter-' + str(i))
    
    return chapter_map