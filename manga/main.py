from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from manga.Episode import Episode

def identify_last_episode(last_watched, manga_name):
    page = requests.get('https://manganelo.com/manga/read_one_piece_manga_online_free4')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup)

    # # Pull all text from the BodyText div
    artist_name_list = soup.find_all(class_='chapter-name text-nowrap', href=True)
    # print(artist_name_list)
    for i in artist_name_list:

        name = i.contents[0]
        link = i.attrs['href']
        episode = link.split("/")[-1]
        episode = float(episode.split("_")[-1])
        if episode > last_watched:
            insert_episode(name, link, episode, manga_name)
        else:
            break
    return True


def insert_episode(name, link, episode, manga_name):
    page = requests.get(link)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver_win32/chromedriver.exe')
    driver.get(link)
    driver.implicitly_wait(1)
    all_imgs = driver.find_elements_by_tag_name("img")
    first_image=0
    all_links= list()
    for i in all_imgs:
        if first_image==0:
            first_image=1
            continue
        all_links.append(i.get_attribute('src'))
    object_episode = Episode()
    object_episode.insert_manga_episode(manga_name, name, episode, all_links)


if __name__ == "__main__":
    identify_last_episode(975, "One Piece")
