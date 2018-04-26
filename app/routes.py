# -*- coding: utf-8 -*-
from flask import render_template,request
from app import app
import sys
#get the path toward the backend folder
sys.path.insert(0, '..')
from backend.interface import SearchInterface

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/', methods=['POST'])
def form_post():
    """Inputs the user request, returns results from interface"""
    text = request.form['text']
    s = SearchInterface()
    s.search_job(text)
    job=s.latest_query
    return u"You searched for: {}".format(s.latest_query)+u"<br/>Best match in taxonomy is: {}".format(s.taxonomy_job)+"<br/>The current prognosis for job is: {}".format(s.current_year_forecast)
if __name__ == '__main__':
    app.run()