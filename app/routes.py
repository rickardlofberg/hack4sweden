from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SearchForm
from app.backend.interface import SearchInterface

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        interface = SearchInterface()
        interface.search_job(form.query.data)
        return render_template('results.html', interface=interface)
    return render_template('index.html', title='Sign In', form=form)

