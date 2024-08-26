from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

with open('datasheet.json') as f:
    json_data = json.load(f)

data = json_data[2]['data']  # Extract the data from the JSON

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    start_date = request.form['startDate']
    end_date = request.form['endDate']
    
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    
    results = []
    for row in data:
        blow_end_time = datetime.strptime(row['BLOW_END_TIME'], "%Y-%m-%d %H:%M:%S")
        if start_date_obj <= blow_end_time <= end_date_obj:
            results.append(row)
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
