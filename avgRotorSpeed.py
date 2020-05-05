#!/bin/python3

import math
import os
import random
import re
import sys

import json
import requests


#
# Complete the 'avgRotorSpeed' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#

def avgRotorSpeed(statusQuery, parentId):
	# Write your code here

	result = requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?status='+statusQuery).json()

	pages=result['total_pages']
	count=0
	soma=0

	for page in range(1, pages+1):
		request=requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?status='+statusQuery+'&page='+str(page)).json()
		data=request['data']

		for i in range(10):
			try:
				idpai=data[i]['parent']['id']
				print('parentId = ' + str(idpai))
				
				if (idpai == parentId):
					rotorSpeed=data[i]['operatingParams']['rotorSpeed']
					print('rotorSpeed = ' + str(rotorSpeed))
					soma=soma+rotorSpeed
					count=count+1
			except:
				pass

	if (soma==0 or count==0):
		return 0
	else:
		rotacao_media=int(soma/count)
		return(rotacao_media)
	

statusQuery = "RUNNING"
parentId = 7

avgRotorSpeed(statusQuery, parentId)
