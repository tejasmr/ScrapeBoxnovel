from tqdm import tqdm
from definitions import NOVEL_URL, TAG_NAME
from driver import driver
from logger import log
from scraper import collect_chapter_content

def get_chapter_count(url=""):
    driver.get(url)
    
    elements = driver.find_elements(by=TAG_NAME, value='a')
    book_name = url.removeprefix(NOVEL_URL)
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
    chapter_map = {}
    for i in tqdm(range(1, count+1)):
        chapter_map[i] = collect_chapter_content(url + '/page/' + i)
        
    return chapter_map