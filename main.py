import json
import time
from tqdm import tqdm
from definitions import CLASS_NAME, CSS_SELECTOR, NOVEL_URL, TAG_NAME
from chapters import get_chapter_content_from_novel, get_chapter_count
from novel_links import write_novel_links
from driver import driver
from scraper import collect_chapter_content

# write_novel_links()
def scrape_boxnovel():
    novel_links = json.load(open('links.json'))
    # print(novel_links)
    novels = {}
    print("novel count =", len(novel_links))
    for i in range(1, len(novel_links)):
        novel_link = novel_links[i]
        novel_chapter_count = get_chapter_count(url=novel_link)
        print(novel_link, novel_chapter_count)
        novel_chapters = {}
        for i in range(1, novel_chapter_count+1):
            novel_chapters[i] = get_chapter_content_from_novel(novel_link + 'chapter/' + str(i))
        novels[novel_link.removeprefix(NOVEL_URL)] = novel_chapters


    with open('novels.json', 'w') as novels_json_file:
        novels_json_file.write(novels)
    print("finished")
    driver.quit()

def scrape_boxnovel_metadata():
    novel_links = json.load(open('links.json'))
    # print(novel_links)
    novels = []

    for novel_link in novel_links:
        print(novel_link)
        driver.get(novel_link)
        time.sleep(2)
        title = driver.title.replace('BoxNovel', 'TezzNovel').replace('boxnovel', 'tezznovel').replace('BOXNOVEL', 'TEZZNOVEL')
        author = driver.find_element(by=CLASS_NAME, value="author-content").find_element(by=CSS_SELECTOR, value="a").text
        
        book_name = novel_link.removeprefix(NOVEL_URL + "/").removesuffix("/")
        elements = driver.find_elements(by=TAG_NAME, value='a')
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
        chapter_count = count
        print(title, author, chapter_count)
        novels.append({"title":title, "author":author, "chapter_count":chapter_count})
    with open('novels.json', 'w') as novels_json_file:
        novels_json_file.write(novels)

if __name__ == "__main__":
    scrape_boxnovel_metadata()
