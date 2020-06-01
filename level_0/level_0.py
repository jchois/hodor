#!/usr/bin/python3
from requests import post
votes = 0
url = 'http://158.69.76.135/level0.php'
payload = {'id': '1657', 'holdthedoor': 'Submit'}
for _ in range(0, 1024):
	r = post(url, data=payload)
	# print(r.status_code, r.reason)
	if r.status_code == 200 and r.reason == 'OK':
		votes +=1
print("You voted {} times for 1657".format(votes))
