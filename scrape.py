import requests
from lxml.html.soupparser import fromstring

def scrape_abc(url):

    print(f"Scraping {url}")

    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False

    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@class, 'Article__Headline__Title')]/text()")[0].strip()
    except:
        title = None
    
    try:    
        desc = tree.xpath("//h2[contains(@class, 'Article__Headline__Desc')]/text()")[0].strip()
    except:
        desc = None

    try:
        article = "\n".join([x.strip() for x in tree.xpath("//section[contains(@class, 'Article__Content story')]/p/text()")])
    except:
        article = None

    return url, title, desc, article



def scrape_fox(url):

    print(f"Scraping {url}")

    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False

    
    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@class, 'headline')]/text()")[0].strip()
    except:
        title = None

    try:    
        desc = tree.xpath("//h2[contains(@class, 'sub-headline speakable')]/text()")[0].strip()
    except:
        desc = None

    try:
        article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'article-body')]/p/text()")])
    except:
        article = None


    return url, title, desc, article


def scrape_cbs(url):
   
    print(f"Scraping {url}")
    
    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False

    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@class, 'content__title')]/text()")[0].strip()
    except:
        title = None

    desc = None
    
    try:
        article = "\n".join([x.strip() for x in tree.xpath("//section[contains(@class, 'content__body')]/p/text()")])
    except:
        article = None

    return url, title, desc, article



def scrape_nbc(url):
    
    print(f"Scraping {url}")
    
    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False
        
    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@class, 'headline')]/text()")[0].strip()
    except:
        title = None

    try:    
        desc = tree.xpath("//div[contains(@class, 'article-dek')]/text()")[0].strip()
    except:
        desc = None
        
    try:
        article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'article-body__content')]/p/text()")])
    except:
        article = None

    return url, title, desc, article


def scrape_cnn(url):
    
    print(f"Scraping {url}")
    
    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False

    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@class, 'headline')]/text()")[0].strip()
    except:
        title = None
        
    desc = None
    
    try:
        article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'body')]/div/text()")])
    except:
        article = None

    return url, title, desc, article

def scrape_bbc(url):
    
    print(f"Scraping {url}")
    
    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False

    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@id, 'main-heading')]/text()")[0].strip()
    except:
        title = None

    desc = None

    try:
        article = "\n".join([x.strip() for x in tree.xpath("//article[contains(@class, 'Article')]/div/div/p/text()")])
    except:
        article = None

    return url, title, desc, article


def scrape_utd(url):
    
    print(f"Scraping {url}")

    try:
        req = requests.get(url, verify=False)
    except:
        print("Problem getting URL")
        return False

    tree = fromstring(req.content)

    try:
        title = tree.xpath("//h1[contains(@class, 'gnt_ar_hl')]/text()")[0].strip()
    except:
        title = None
    
    desc = None
    
    try:
        article = "\n".join([x.strip() for x in tree.xpath("//div[contains(@class, 'gnt_ar_b')]/p/text()")])
    except:
        article = None

    return url, title, desc, article





