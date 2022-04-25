from logger import log
from definitions import CLASS_NAME, NOVEL_URL
from driver import driver
from scraper import collect_links
import json
from tqdm import tqdm

def get_novel_count():
    log("[START] Getting novel count...")
    driver.get(NOVEL_URL)
    log("[FINSH] Getting novel count...")
    return int(driver.find_elements(by=CLASS_NAME, value="h4")[1].text.split(sep=' ')[0]) 

def write_novel_links():
    links = set()
    count = get_novel_count() // 10 + 1
    
    log("[START] Getting novel links")
    for i in tqdm(range(1, count+1)):
        collect_links(NOVEL_URL + "/page/" + str(i), links=links)
        
    links.remove(NOVEL_URL + "/")
    links.remove(NOVEL_URL + "/#")
    log("[FINSH] Getting novel links")
    print(len(links))
    log("[START] Writing json file")
    links_json = json.dumps(list(links), indent=4)
    with open('links.json', 'w') as links_json_file:
        links_json_file.write(links_json)
    log("[FINSH] Writing json file")