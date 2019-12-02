from flask import render_template as show
from app import timetable
from app import app
import json

tt = timetable.Timetable('app/request_json.json')
data = tt.build_table()


@app.route('/')
def index():
	return show('index.html', data=data)


@app.route('/get/<event_id>', methods=['POST'])
def get(event_id):
	h, d = map(int, event_id.split("D"))
	
	return json.dumps(data[h][d]['full_info'])
	# return data[h][d]['full_info']
