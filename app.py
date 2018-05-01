import os
from flask import Flask, request, render_template,jsonify
from airtable import Airtable

AT= Airtable('Airtable Base Key',
            'Skills',
            'Airtable API Key')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/search')
def rate():
    #query = request.args.get('query')
    search_result=AT.get_all()
    return jsonify(search_result)
    


if __name__ == '__main__':
   app.run()