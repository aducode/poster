#!/usr/bin/python
# -*- coding:utf-8 -*-
"""A simple poster for use Github Pages as Blog"""
import markdown2
import sys
	
def init():
	"""
	init github pages
	
	"""
	print 'init'
	

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

	
