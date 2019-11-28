from flask import render_template as show
from app import timetable
from app import app

@app.route('/')
def index():
	tt = timetable.Timetable('app/request_json.json')
	return show('index.html', tt=tt.data)
