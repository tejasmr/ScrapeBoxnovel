import time
from definitions import TAG_NAME
from driver import driver
from logger import log

def collect_links(url="", links=set()):
    driver.get(url)
    elements = driver.find_elements(by=TAG_NAME, value='a')
    for element in elements:
        link = element.get_attribute('href')
        if link is None:
            continue
        if not '/novel/' in link:
            continue
        if '/novel/?' in link:
            continue
        if 'chapter' in link:
            continue
        if '?' in link:
            continue
        if '/page/' in link:
            continue
        links.add(link)

def collect_chapter_content(url=""):
    driver.get(url)
    # time.sleep(0.5)
    elements = driver.find_elements(by=TAG_NAME, value='p')
    output_text = ""
    for element in elements:
        text = element.text
        if '' == text:
            continue
        if '<' in text:
            continue
        if 'boxnovel' in text:
            continue
        if 'BOXNOVEL' in text:
            continue
        if 'Translator' in text and 'Editor' in text:
            continue
        output_text += text + '\n'
    print(len(output_text))
    return output_text