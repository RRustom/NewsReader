import os, feedparser, unidecode, re
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
from flask_navigation import Navigation

from .newsreader import Feed, News, BehindNews, Data, Tutorials, SocialMedia

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    nav = Navigation(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Navigation Bar
    nav.Bar('top', [
        nav.Item('Home', 'home'),
        nav.Item('Headline News', 'news'),#, {'page': 1}),
        nav.Item('Behind the Headline', 'behind_news'),
        nav.Item('Data', 'data'),
        nav.Item('Social Media', 'social_media'),
        nav.Item('Tutorials', 'tutorials'),
        nav.Item('Other', 'other')
        ])

    @app.context_processor
    def utility_processor():
        def clean_summary(summary):
            """
            Cleans up the summary for each entry from HTML tags.
            """
            delimiters="<div", "<img"
            regex_pattern = '|'.join(map(re.escape, delimiters))
            split_list = re.split(regex_pattern, summary)

            if len(split_list[0])<600:
                return split_list[0]
            else:
                return "Summary too long. Click the link for more info"
        def image_link(entry):
            """
            Get image from entry[i].links
            """
            for link in entry.links:
                if "image" in link.type:
                    return link.href
        return dict(clean_summary=clean_summary, image_link=image_link)

    # Home
    @app.route('/')
    def home():
        """
        TODO: highlights (top 3) from each section
        """
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', feed=entries)

    # Headline News
    @app.route('/headlines')
    def news():
        """
        Topics:
        1. Technology
            - Security
            - Machine Learning + Data Analysis
            - Systems / Software
            - AGT
            - Networks / Optimization
        2. Math
            - Probability
            - ACT
            - Pure Math
        3. Geopolitics
        4. business
        5. VC/Silicon Valley
        6. Payments
        7. Finance
        8. architecture / urban planning
        9. cities
        10. Sports
        11. MENA
        12. Developing World
        13. Startup / Management
        14. Construction / Real Estate
        15. Philosophy
        """
        feed = News()
        entries = feed.entries()
        return render_template('index.html', name="Headline News", feed=entries)

    # @app.route('/headlines/<int:page>')
    # def news(page):
    #     return render_template('news.html', page=page)

    # Behind the Headlines
    @app.route('/behind')
    def behind_news():
        """
        Same topics, different sources:
        1. Technology
            - Security
            - Machine Learning + Data Analysis
            - Systems / Software
            - AGT
            - Networks / Optimization
        2. Math
            - Probability
            - ACT
            - Pure Math
        3. Geopolitics
        4. business
        5. VC/Silicon Valley
        6. Payments
        7. Finance
        8. architecture / urban planning
        9. cities
        10. Sports
        11. MENA
        12. Developing World
        13. Startup / Management
        14. Construction / Real Estate
        15. Philosophy
        16. History
        17. Music
        """
        feed = BehindNews()
        entries = feed.entries()
        return render_template('index.html', name="Behind the Headlines", feed=entries)

    # Behind the Headlines
    @app.route('/data')
    def data():
        feed = Data()
        entries = feed.entries()
        return render_template('index.html', name="Data", feed=entries)

    # Social Media
    @app.route('/social')
    def social_media():
        feed = SocialMedia()
        entries = feed.entries()
        #print("ENTRIES: ", entries)
        return render_template('social.html', name="Social Media", feed=entries)

    # Tutorials
    @app.route('/tutorials')
    def tutorials():
        feed = Tutorials()
        entries = feed.entries()
        return render_template('index.html', name="Tutorials", feed=entries)

    # Other Media
    @app.route('/other')
    def other():
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', name="Other", feed=entries)

    return app
