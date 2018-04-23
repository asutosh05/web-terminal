import os
from flask import Flask, request, render_template
from airtable import Airtable

AT= Airtable('app18kAON3MzboLOJ',
            'Skills',
            'keyxk901dRG3cMf4a')
app = Flask(__name__)

@app.route('/')
def index():
    search_result=AT.get_all()
    return render_template('index.html',)

if __name__ == '__main__':
   app.run()