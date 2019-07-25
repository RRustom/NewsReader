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
        self._sources = {}

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

# class Topic:
#     """
#     A class representing a single topic within a Feed.
#     """
#     def __init__(self):
#         """
#         """
#         self._source = {}
#
#     def

class News(Feed):
    """
    Mainstreem news
    """
    def __init__(self):
        """
        """
        self._sources = {
            "CNN": "http://rss.cnn.com/rss/cnn_world.rss",
            #TODO: AP News, AFP
            "Reuters World": "http://feeds.reuters.com/Reuters/worldNews",
            "Reuters Business": "http://feeds.reuters.com/reuters/businessNews",
            #"The New Republic": "https://www.newrepublic.com/rss.xml",
            "BW Venture Capital": "https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJdEVhZXw==",
            "Zawya Regional": "https://www.zawya.com/rssfeeds/regional.xml",
            "Vox": "https://www.vox.com/rss/index.xml"
            }

class BehindNews(Feed):
    """
    Different opinions
    """
    def __init__(self):
        """
        """
        self._sources = {
            # thealeppoproject.com
            # https://openai.com/blog/
            # jadaliyya.com
            # barabasilab.com
            # fin.plaid.com

            # Tech
            "Hacker Noon": "https://medium.com/feed/hackernoon",
            "Fast Company": "www.fastcompany.com/section/rss.xml",
            "Tensorflow": "https://medium.com/feed/tensorflow",
            "FinExtra": "www.finextra.com/rss/headlines.aspx",
            # Politics
            "National Review": "https://www.nationalreview.com/feed/",
            "Hugh Hewitt": "https://www.hughhewitt.com/columns/feed/",
            "Michael Medved": "http://www.michaelmedved.com/feed/?post_type=column",
            # Science / Math / Research
            "Distill": "https://distill.pub/rss.xml",
            "Quanta Magazine": "https://api.quantamagazine.org/feed/",
            "Autodesk Research": "https://autodeskresearch.com/rss/publications",
            "IEEE SPectrum": "https://spectrum.ieee.org/rss/fulltext",
            #Cities
            "CityLab": "https://www.citylab.com/feeds/posts/",
            "Curbed": "https://www.curbed.com/rss/index.xml",
            "BRIK": "https://www.brikbase.org/rss.xml",
            #Security
            "Threat Post": "https://threatpost.com/feed/"
            }

class Data(Feed):
    def __init__(self):
        """
        """
        self._sources = {
            "CNN": "http://rss.cnn.com/rss/cnn_world.rss",
            #TODO: AP News, AFP
            "Reuters World": "http://feeds.reuters.com/Reuters/worldNews",
            "Reuters Business": "http://feeds.reuters.com/reuters/businessNews",
            #"The New Republic": "https://www.newrepublic.com/rss.xml",
            "BW Venture Capital": "https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJdEVhZXw==",
            "Zawya Regional": "https://www.zawya.com/rssfeeds/regional.xml",
            }

class Tutorials(Feed):
    def __init__(self):
        """
        """
        self._sources = {
            "CNN": "http://rss.cnn.com/rss/cnn_world.rss",
            #TODO: AP News, AFP
            "Reuters World": "http://feeds.reuters.com/Reuters/worldNews",
            "Reuters Business": "http://feeds.reuters.com/reuters/businessNews",
            #"The New Republic": "https://www.newrepublic.com/rss.xml",
            "BW Venture Capital": "https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJdEVhZXw==",
            "Zawya Regional": "https://www.zawya.com/rssfeeds/regional.xml"
            }

class SocialMedia(Feed):
    def __init__(self):
        """
        """
        self._sources = {
            "_structerra":"https://queryfeed.net/instagram?q=_structerra",
            "steelcase": "https://queryfeed.net/instagram?q=steelcase"
            }
