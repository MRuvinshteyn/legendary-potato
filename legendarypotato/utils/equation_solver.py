#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET


def getRes(input):
    server = 'http://api.wolframalpha.com/v2/query?'
    appid = '6QYPX8-HUAE3WKH7J'
    input = 'solve'+input
    answer = {}
    queryStr = server + 'appid=' + appid + '&podstate=Result__Step-by-step+solution'

    #print(requests.api.get(queryStr).content)
    results = ET.fromstring((requests.api.get(queryStr, params= {'input' : input} ).content))
    if results.attrib['success'] != 'false':

        for child in results:
            if 'title' in child.attrib.keys():
                if child.attrib['title'] == 'Input interpretation' or child.attrib['title'] == 'Input':
                    for child2 in child:
                        if str(child2.tag) == 'subpod':
                            for child3 in child2:
                                if child3.tag == 'img':
                                    answer[child.attrib['title'] + '_img'] = child3.attrib['src']
                                else:
                                    answer[child.attrib['title'] + '_text'] = child3.text
                if child.attrib['title'] == 'Results' or child.attrib['title'] == 'Exact result' or child.attrib['title'] == 'Decimal form' or child.attrib['title'] == 'Answer':
                    for child2 in child:
                        if str(child2.tag) == 'subpod':
                            for child3 in child2:
                                if child3.tag == 'img':
                                    answer[child.attrib['title'] + '_img'] = child3.attrib['src']
                                else:
                                    answer[child.attrib['title'] + '_text'] = child3.text
                                    break
                if "Reference" in child.attrib['title'] or "Exact Solution" in child.attrib['title'] or "Plot" in child.attrib['title']:
                    for child2 in child:
                        for child3 in child2:
                            if child3.tag == 'plaintext':
                                answer[child.attrib['title'] + '_text'] = child3.text
                            if child3.tag == 'img':
                                answer[child.attrib['title'] + '_img'] = child3.attrib['src']
    else:
        print("The equation cannot be solved as written")
        for child in results:
            for child2 in child:
                print("did you mean: " + child2.text + " ?")

    return answer

print(getRes("2x - 3 + 8y = 87"))