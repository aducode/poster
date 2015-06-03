#!/usr/bin/python
# -*- coding:utf-8 -*-
"""A simple poster for use Github Pages as Blog"""
import sys
import os
import markdown2

LAYOUT_PATH='$layout'
DEFAULT_LAYOUT='default.layout'

POST_PATH='$post'


def init():
	"""
	init github pages
	
	"""
	if not os.path.exists(LAYOUT_PATH):
		os.makedirs(LAYOUT_PATH)
	layout_file = os.path.join(LAYOUT_PATH, DEFAULT_LAYOUT)
	if not os.path.isfile(layout_file):
		with open(layout_file,'w') as layout:
			layout.write('\n'.join([
			'<!DOCTYPE html>',
			'<html>',
			'<head>',
			'<meta charset="utf-8"/>',
			'<meta http-equiv="X-UA-Compatible" content="chrome=1"/>',
			'<!-- css -->',
			'<!-- title -->',
			'<title>{title}</title>',
			'</head>',
			'<body>',
			'<!-- content -->',
			'{content}',
			'</body>',
			'</html>',
			]))
	if not os.path.exists(POST_PATH):
		os.makedirs(POST_PATH)
	

def list(title=None, date=None):
	"""
	list all the blogs
	:param title: blog title
	:param date:  blog created/modified date
	:return
	"""
	print 'list ', title, ' ', date

def create(title, date=None):
	"""
	create a new blog
	:param title: blog's title
	:param date:  created date
	:return
	"""
	print 'create ', title, ' ', date

def edit(title, date=None):
	"""
	edit blog
	:param tilte: blog title
	:param date: blog created/modified date
	:return
	"""
	print 'edit ', title, ' ', date
	
	
def remove(title, date=None):
	"""
	remove blog
	:param title: blog's title
	:param date: blog created/modified date
	:return
	"""
	print 'remove ', title, ' ', date
	

	
def usage():
	"""
	print usage and exit
	"""
	usage = [
		'Usage:',
		'\tpython poster action title [date]',
		'',
		'action list:'
		'\tinit: init github pages',
		'\tcreate: create new blog',
		'\tedit: edit exist blog',
		'\tremove: remove exist blog',
		'\tlist: list blog',
	]
	print '\n'.join(usage)
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv)>=2 and sys.argv[1] == 'init':
		init()
	elif len(sys.argv)>=2 and sys.argv[1] != 'init':
		action = sys.argv[1]
		title = None
		date = None
		if len(sys.argv)>=3:
			title = sys.argv[2]
		if len(sys.argv)>=4:
			title = sys.argv[4]
		globals()[action](title, date)
	else:
		usage()

	
