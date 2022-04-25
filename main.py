import json
from tqdm import tqdm
from definitions import NOVEL_URL
from chapters import get_chapter_content_from_novel, get_chapter_count
from novel_links import write_novel_links
from driver import driver
from scraper import collect_chapter_content

if __name__ == "__main__":
    # write_novel_links()
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
