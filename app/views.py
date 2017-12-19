# views.py

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/watson_nlc')
def watson_nlc():
    
    import json
    from watson_developer_cloud import NaturalLanguageUnderstandingV1
    from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions

    from ConfigParser import SafeConfigParser
    config = SafeConfigParser()
    config.read('/etc/watson_cfg.ini')

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username=config.get('watson', 'username'),
        password=config.get('watson', 'password'),
        version=config.get('watson', 'version')
    )

    response = natural_language_understanding.analyze(
        url='https://fr.wikipedia.org/wiki/Gen%C3%A8ve',
        features=Features(
            categories=CategoriesOptions()
        )
    )

    return(json.dumps(response))
