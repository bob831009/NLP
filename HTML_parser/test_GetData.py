#! -*- coding: utf-8 -*-
import urllib, urllib2
from bs4 import BeautifulSoup
from Tkinter import *
import tkFileDialog

Tk().withdraw()
options = {}
options['multiple'] = False

options['title'] = "input file"
inputDir = tkFileDialog.askopenfilenames(**options)
inputDir = str(inputDir).strip("(),'")
input_file = open(inputDir , 'r')

options['title'] = "output file"
outputDir = tkFileDialog.askopenfilenames(**options)
outputDir = str(outputDir).strip("(),'")
output_file = open(outputDir , 'w')

for line in input_file.readlines():
    line = line.strip(' \n')
    print line
    if not len(line) and line.startswith('#'):
        continue
    else:
        url = line
        req = urllib2.Request(url)
        u = urllib2.urlopen(req)
        soup = BeautifulSoup(u, 'html.parser')
        output_file.write(str(line)+"\n")
        output_file.write("-------------------------------\n")
        for remove_data in soup("script"):
            remove_data.decompose()
        for remove_data in soup("style"):
            remove_data.decompose()
        for data in soup.stripped_strings:
            data = data.encode('utf-8')
            output_file.write(str(data)+'\n')

