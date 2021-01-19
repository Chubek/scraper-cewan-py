import feedparser
from lxml.html.soupparser import parse
from scrape import *
import functools
import operator

def parse_abc():
    feeds = [
        'http://feeds.abcnews.com/abcnews/topstories',
        'http://feeds.abcnews.com/abcnews/internationalheadlines',
        'https://abcnews.go.com/abcnews/usheadlines',
        'https://abcnews.go.com/abcnews/politicsheadlines'
    ]
    print("Scraping ABC... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_abc(x.link.strip()) for x in feedparser.parse(y).entries] for y in feeds], [])


def parse_fox():
    feeds = [
        'http://feeds.foxnews.com/foxnews/latest',
        'http://feeds.foxnews.com/foxnews/world',
        'http://feeds.foxnews.com/foxnews/national',
        'http://feeds.foxnews.com/foxnews/politics'
    ]
    print("Scraping FOX... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_fox(x.link.strip()) for x in feedparser.parse(y).entries] for y in feeds], [])

def parse_cbs():
    feeds = [
        'https://www.cbsnews.com/latest/rss/main',
        'https://www.cbsnews.com/latest/rss/us',
        'https://www.cbsnews.com/latest/rss/politics',
        'https://www.cbsnews.com/latest/rss/world'
    ]
    print("Scraping CBS... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_cbs(x.link.strip()) for x in feedparser.parse(y).entries] for y in feeds], [])


def parse_nbc():
    feeds = [
        'http://feeds.nbcnews.com/nbcnews/public/news',
        'http://feeds.nbcnews.com/nbcnews/public/world',
        'http://feeds.nbcnews.com/nbcnews/public/politics',
    ]
    print("Scraping NBC... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_nbc(x.link.strip()) for x in feedparser.parse(y).entries] for y in feeds], [])


def parse_cnn():
    feeds = [
        'http://rss.cnn.com/rss/cnn_topstories.rss',
        'http://rss.cnn.com/rss/cnn_world.rss',
        'http://rss.cnn.com/rss/cnn_us.rss',
    ]
    print("Scraping CNN... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_cnn(x.link.strip()) for x in feedparser.parse(y).entries] for y in feeds], [])


def parse_bbc():
    feeds = [
        'http://feeds.bbci.co.uk/news/rss.xml',
        'http://feeds.bbci.co.uk/news/world/rss.xml',
        'http://feeds.bbci.co.uk/news/uk/rss.xml',
        'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml'
    ]
    print("Scraping BBC... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_bbc(x.link.strip()) for x in feedparser.parse(y).entries[:1]] for y in feeds], [])


def parse_utd():
    feeds = [
        'http://rssfeeds.usatoday.com/usatoday-NewsTopStories',
        'http://rssfeeds.usatoday.com/UsatodaycomWorld-TopStories',
        'http://rssfeeds.usatoday.com/UsatodaycomNation-TopStories',
    ]
    print("Scraping USA Today... Please wait...")
    return functools.reduce(operator.iconcat, [[scrape_utd(x.link.strip()) for x in feedparser.parse(y).entries] for y in feeds], [])


