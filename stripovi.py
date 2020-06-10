import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen as uReq
import time

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
# gde ovde treba da proverava da li je .img ili sve ostalo sto ne treba!!
def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    return urls

def download(url, pathname):
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    buffer_size = 99
    filename = os.path.join(pathname, url.split("/")[-1])
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))
    # printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    # for i, item in enumerate(items):
    #     time.sleep(0.1)
    #     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


def main(url, path):
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)

    delete_png = os.listdir(path)
    for item in delete_png:
        if item.endswith(".png"):
            os.remove(os.path.join(path, item))



def cela_strana(sajt):
    myUrl = sajt

    uClient = uReq(myUrl)
    page_html = uClient.read()
    uClient.close()
    page_soup = bs(page_html, 'html.parser')

    containers = page_soup.findAll('div', {'class':'post-body entry-content'})
    a_tag = containers[0].findAll('a')


    for a_tag_single in a_tag:
        if(a_tag_single['href'].split('.')[::-1][0] == 'html'):
            strip_strana = a_tag_single['href']
            ime_foldera = a_tag_single.text
            main(strip_strana, ime_foldera)
        else:
            continue



sajt = input("Enter site --- ")
cela_strana(sajt)
