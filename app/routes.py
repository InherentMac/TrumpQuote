from app import app
from flask import render_template
import requests
import json
import calendar

@app.route('/')
def index():
    res = requests.get('https://api.tronalddump.io/random/quote').text
    quote = json.loads(res)
    date = [quote['_embedded']['source'][0]['created_at'].split('T')[0].split('-')[0], calendar.month_abbr[int(quote['_embedded']['source'][0]['created_at'].split('T')[0].split('-')[1])]]
    return render_template('index.html', title='TrumpQuote', quote=quote, date=date)