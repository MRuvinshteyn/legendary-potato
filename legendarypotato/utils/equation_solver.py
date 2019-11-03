#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET


def getRes(input):
    server = 'http://api.wolframalpha.com/v2/query?' #Where the api call is made from
    appid = '6QYPX8-3U42KRYWEH' #API key - may have problems with git, try not to commit with this still filled
    input = 'solve'+input #Formatted input for  query param
    answer = {'input_img': "", 'answer_img' : "", 'acceptable_answers': []} #initial answer dictionary
    queryStr = server + 'appid=' + appid + '&podstate=Result__Step-by-step+solution' #Near complete query string - input

    #print(requests.api.get(queryStr).content)
    results = ET.fromstring((requests.api.get(queryStr, params= {'input' : input} ).content)) # Call the api and recieve xml
    if results.attrib['success'] != 'false': #Make sure the call was successful

        for child in results: #Iterate through the different xml sections

            if 'title' in child.attrib.keys(): #Filter out irrelevant XML sections
                if child.attrib['title'] == 'Input interpretation' or child.attrib['title'] == 'Input': #Scan for the initial equation
                    for child2 in child:    #Dig through more xml
                        if str(child2.tag) == 'subpod': #Find relevant tags
                            for child3 in child2: #dig through more xml
                                if child3.tag == 'img': #add the image link to the dictionary
                                    answer['input_img'] = child3.attrib['src']
                                else: #add the plaintext to the dictionary
                                    answer[child.attrib['title'] + '_text'] = child3.text
                if child.attrib['title'] == 'Results' or child.attrib['title'] == 'Exact result' or child.attrib['title'] == 'Decimal form' or child.attrib['title'] == 'Answer': #Scan for the Result
                    for child2 in child:
                        if str(child2.tag) == 'subpod':
                            for child3 in child2:
                                if child3.tag == 'img':
                                    answer['answer_img'] = child3.attrib['src']
                                else:
                                    answer['acceptable_answers'].append(str(child3.text.split("\n").pop()).strip('|')) # add the plaintext answer to the list of acceptable answers

                if "Reference" in child.attrib['title'] or "solution" in child.attrib['title'] or "Plot" in child.attrib['title'] or "Solution" in child.attrib['title']: #Scan for mostly trig and algebra stuff
                    for child2 in child:
                        for child3 in child2:
                            if child3.tag == 'plaintext':
                                answer[child.attrib['title'] + '_text'] = child3.text
                            if child3.tag == 'img':
                                answer[child.attrib['title'] + '_img'] = child3.attrib['src']
    else:
        print("The equation cannot be solved as written") #throw an error if the API is broken or the equation is improperly formatted
        for child in results:
            for child2 in child:
                print("did you mean: " + child2.text + " ?")

    return answer

print(getRes(' x^2 - 3x + 8 '))