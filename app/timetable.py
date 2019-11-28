import requests, json
from pprint import pprint
from datetime import datetime
from collections import defaultdict

URL = "https://opentimetable.dcu.ie/broker/api/categoryTypes/241e4d36-60e0-49f8-b27e-99416745d98d/categories/events/filter"

HEADERS = {
	"Authorization": "basic T64Mdy7m[",
	"Content-Type" : "application/json; charset=utf-8",
	"credentials": "include",
	"Referer" : "https://opentimetable.dcu.ie/",
	"Origin" : "https://opentimetable.dcu.ie/"
}



class Timetable():
	def __init__(self, request):
		with open(request, 'r') as f:
			request = json.loads(f.read())
		
		res = requests.post(URL, json=request, headers=HEADERS)
		self.data = self.format(res.json())


	def __str__(self):
		for day in sorted(self.lecs):
			print(f"-------------{day}-------------\n")
			for lec in self.lecs[day]:
				print(lec['Description'])
				print(self.totime(lec['StartDateTime']).hour)		

	def totime(self, t):
		return datetime.strptime(t[:-3], "%Y-%m-%dT%H:%M:%S+%f")


	def format(self, data):
		d = data[0]
		lecs = defaultdict(dict)
		for e in d['CategoryEvents']:
			start = self.totime(e['StartDateTime'])
			lecs[start.hour][start.weekday()] = e

		return dict(lecs)



def main():
	tt = Timetable('request_json.json')
	print(json.dumps(tt.data))
	# d = ['mon', 'tue', 'wed', 'thur', 'fri']
	# for k in sorted(tt.data):
	# 	print(d[k], *sorted(tt.data[k]))

# lecs[start.strftime('%A')].append(e)

if __name__ == '__main__':
	main()
