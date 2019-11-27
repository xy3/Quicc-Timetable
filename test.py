import requests, json
from pprint import pprint
from datetime import datetime

URL = "https://opentimetable.dcu.ie/broker/api/categoryTypes/241e4d36-60e0-49f8-b27e-99416745d98d/categories/events/filter"

HEADERS = {
	"Authorization": "basic T64Mdy7m[",
	"Content-Type" : "application/json; charset=utf-8",
	"credentials": "include",
	"Referer" : "https://opentimetable.dcu.ie/",
	"Origin" : "https://opentimetable.dcu.ie/"
}



def timetable(json_payload):
	with open(json_payload, 'r') as f:
		request_payload = json.loads(f.read())
	
	res = requests.post(URL, json=request_payload, headers=HEADERS)
	d = res.json()
	
	return d


def format_time(t):
	return datetime.strptime(t[:-3], "%Y-%m-%dT%H:%M:%S+%f")


def main():
	tt = timetable('json_payload.json')
	# print(json.dumps(tt))
	d = tt[0]

	lectures = {}

	print(d["Name"])
	for e in d['CategoryEvents']:
		print(f"{e['Name'][:5]} - {e['Description']}")
		print(e['EventType'])
		print(e['Location'])

		start = format_time(e['StartDateTime'])
		end = format_time(e['EndDateTime'])

		print(start.strftime('%A'))
		
		print("==========")

main()
