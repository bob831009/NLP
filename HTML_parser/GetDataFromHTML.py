# -*-coding: utf-8-*-
import urllib, urllib2, cookielib
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from Tkinter import *
import tkFileDialog

# input_file = open('test_data' , 'r')
# output_file = open('output_data' , 'w')

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


class MyHTMLParser(HTMLParser):
	# def handle_starttag(self , tag , attrs):
	# 	value = "Start tag: " + str(tag) + '\n'
	# 	output_file.write(str(value))
	# 	for attr in attrs:
	# 		value = "    attr: " + str(attr) + '\n'
	# 		output_file.write(str(value))
	# def handle_endtag(self, tag):
	# 	value = "End tag  : " + str(tag) + '\n'
	# 	output_file.write(str(value))
	def handle_data(self, data):
		data = str(data)
		data = data.strip()
		if len(data) and not data.startswith('\n') and not data.startswith(' '):
			output_file.write(data+'\n')
	# def handle_comment(self, data):
	# 	print "Comment!"
	# def handle_comment(self, data):
	# 	output_file.write("Comment  :"+str(data)+'\n')
	# 	print "Comment!"
	# def handle_entityref(self, name):
	# 	c = unichr(name2codepoint[name])
	# 	output_file.write("Named ent:" + c)
	# 	print "Named ent:", c
	# def handle_charref(self, name):
	# 	if(name.startswith('x')):
	# 		c = unichr(int(name[1:], 16))
	# 	else:
	# 		c = unichr(int(name))
	# 	output_file.write("Num ent  :"+ c)
	# 	print "Named ent:", c
	# def handle_decl(self, data):
	# 	print "decl"
	# 	output_file.write("Decl     :"+str(data))

Page_parser = MyHTMLParser()

#連到其他頁面

for line in input_file.readlines():
	line = line.strip(" \n")
	print line
	if not len(line) and line.startswith('#'):
		continue
	else:
		url = line
		req = urllib2.Request(url)
		u = urllib2.urlopen(req)
		webContent = u.read()
		output_file.write(str(line)+"\n")
		output_file.write("-------------------------------\n")
		Page_parser.feed(webContent)


