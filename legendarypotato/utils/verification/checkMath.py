#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET


def getRes(input):
	server = 'http://api.wolframalpha.com/v2/query?'
	appid = '6QYPX8-HUAE3WKH7J'
	input = 'solve'+input
	answer = list()
	queryStr = server + 'appid=' + appid + '&input=solve' + input + '&podstate=Result__Step-by-step+solution&format=plaintext'

	print(requests.api.get(queryStr).content)
	results = ET.fromstring((requests.api.get(queryStr).content))
	for child in results:
		print(child.attrib['title'])
		if child.attrib['title'] == 'Input interpretation':
			for child2 in child:
				print(child2.tag)
				if str(child2.tag) == 'subpod':
					for child3 in child2:
						print(child3.text)
						answer.append(child3.text)
		if child.attrib['title'] == 'Results':
			for child2 in child:
				print(child2.tag)
				if str(child2.tag) == 'subpod':
					for child3 in child2:
						print(child3.text)
						answer.append(child3.text)

	return answer

#print(getRes('+3x-7%3D11'))

