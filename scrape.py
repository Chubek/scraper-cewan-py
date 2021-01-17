import requests
from lxml.html.soupparser import fromstring

def scrape_abc(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@class, 'Article__Headline__Title')]/text()")[0].strip()

    desc = tree.xpath("//h2[contains(@class, 'Article__Headline__Desc')]/text()")[0].strip()

    article = "\n".join([x.strip() for x in tree.xpath("//section[contains(@class, 'Article__Content story')]/p/text()")])


    return title, desc, article



def scrape_fox(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@class, 'headline')]/text()")[0].strip()

    desc = tree.xpath("//h2[contains(@class, 'sub-headline speakable')]/text()")[0].strip()

    article = "\n".join([x.strip() for x in tree.xpath("//section[contains(@class, 'article-body')]/p/text()")])


    return title, desc, article


def scrape_cbs(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@class, 'content__title')]/text()")[0].strip()

    desc = None

    article = "\n".join([x.strip() for x in tree.xpath("//section[contains(@class, 'content__body')]/p/text()")])


    return title, desc, article



def scrape_nbc(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@class, 'headline')]/text()")[0].strip()

    desc = tree.xpath("//div[contains(@class, 'article-dek')]/text()")[0].strip()

    article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'article-body__content')]/p/text()")])


    return title, desc, article


def scrape_cnn(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@class, 'headline')]/text()")[0].strip()

    desc = None

    article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'body')]/div/text()")])


    return title, desc, article

def scrape_bbc(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@id, 'main-heading')]/text()")[0].strip()

    desc = None

    article = "\n".join([x.strip() for x in tree.xpath("//article[contains(@class, 'Article')]/div/div/p/text()")])


    return title, desc, article


def scrape_utd(url):
    req = requests.get(url)

    tree = fromstring(req.content)

    title = tree.xpath("//h1[contains(@class, 'gnt_ar_hl')]/text()")[0].strip()

    desc = None

    article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'gnt_ar_b')]/p/text()")])


    return title, desc, article

print(scrape_utd("https://www.usatoday.com/story/news/nation/2021/01/15/national-guards-no-show-capitol-riots-shows-lack-preparation/4169368001/")) 



