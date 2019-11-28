from flask import render_template as show
from app import timetable
from app import app

@app.route('/')
def index():
	tt = timetable.Timetable('app/request_json.json')
	data = tt.build_table()
	return show('index.html', data=data)
