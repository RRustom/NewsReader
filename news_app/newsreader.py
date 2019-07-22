import feedparser, unidecode, os
#import xml.etree.ElementTree as ET

# feedparser info: https://pythonhosted.org/feedparser/
class Feed:
    """
    Class for a news feed.

    Sources:
    - News sites
    - blogs/ personal pages
    - GitHub
    - Reports
    - Academic Papers/Journals

    Outline:
    News:
    1. Headline News
        - Sports
        - Finance/Stocks
        - Geopolitics
        - Film
    2. Behind the Headline News

    3. Social Media:
        - Instagram (the accounts I care about)
    4. Tutorials

    5. Other Media:
    -
    """
    def __init__(self):
        """
        """
        self._sources = {
            "CNN": "http://rss.cnn.com/rss/cnn_world.rss",
            #TODO: AP News, AFP
            "Reuters World": "http://feeds.reuters.com/Reuters/worldNews",
            "Reuters Business": "http://feeds.reuters.com/reuters/businessNews",
            "The New Republic": "https://www.newrepublic.com/rss.xml",
            "BW Venture Capital": "https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJdEVhZXw==",
            "Zawya Regional": "https://www.zawya.com/rssfeeds/regional.xml"
            }

    # @property.setter
    # def sources(self, source):

    def entries(self):
        """
        """
        entries = {}
        for source_name, source in self._sources.items():
            feed = feedparser.parse(source)
            entries[source_name] = feed.entries
        return entries


class News(Feed):
    """
    """

class BehindNews(Feed):
    """
    """
