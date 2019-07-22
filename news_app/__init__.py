import os, feedparser, unidecode
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
from flask_navigation import Navigation

from .newsreader import Feed

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
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', name="Headline News", feed=entries)

    # @app.route('/headlines/<int:page>')
    # def news(page):
    #     return render_template('news.html', page=page)

    # Behind the Headlines
    @app.route('/behind')
    def behind_news():
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', feed=entries)

    # Behind the Headlines
    @app.route('/data')
    def data():
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', feed=entries)

    # Social Media
    @app.route('/social')
    def social_media():
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', feed=entries)

    # Tutorials
    @app.route('/tutorials')
    def tutorials():
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', feed=entries)

    # Other Media
    @app.route('/other')
    def other():
        feed = Feed()
        entries = feed.entries()
        return render_template('index.html', feed=entries)

    return app
