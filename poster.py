#!/usr/bin/python
# -*- coding:utf-8 -*-
"""A simple poster for use Github Pages as Blog"""
import sys
import os
import datetime
import shutil
import markdown2

LAYOUT_PATH='.layout'
DEFAULT_LAYOUT='default.layout'

POST_PATH='.posts'

INDEX='.id'

DATE_FMT='%Y-%m-%d'


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
			'',
			]))
	if not os.path.exists(POST_PATH):
		os.makedirs(POST_PATH)
	if not os.path.exists(INDEX):
		with open(INDEX,'w') as idfile:
			idfile.write('\n'.join([
			'#0',		# 保存最大索引
			'',
			]))


def clear():
	"""
	clear
	"""
	flag=raw_input('Will remove generated files,continue?[Y/N]:')
	if flag != 'Y' and flag != 'y':
		return
	if os.path.exists(LAYOUT_PATH):
		shutil.rmtree(LAYOUT_PATH)
	if os.path.exists(POST_PATH):
		shutil.rmtree(POST_PATH)
	if os.path.isfile(INDEX):
		os.remove(INDEX)


def list(title=None, date=None):
	"""
	list all the blogs
	:param title: blog title
	:param date:  blog created/modified date
	:return
	"""
	if not os.path.isfile(INDEX):
		print '%s not found' % INDEX
		return
	ret={}
	with open(INDEX) as id:
		for line in id:
			line=line.rstrip()
			if not line.startswith('#') and line:
				token=line.split()
				_id = int(token[0])
				_title=token[1]
				_date=token[2]
				if title is not None:
					if _title==title:
						if date is not None:
							if _date==date:
								ret[_id]=(_title, _date)
						else:
							ret[_id]=(_title, _date)
				else:
					ret[_id]=(_title, _date)
	for k, v in ret.items():
		print k,'\t','%s\t%s' % v
	return ret if ret else None


def create(title, date):
	"""
	create a new blog
	:param title: blog's title
	:param date:  created date
	:return
	"""
	if not title:
		print '[!]title is required'
		return
	if date is None:
		date = datetime.datetime.now().strftime(DATE_FMT)
	r = list(title, date)	
	if r is not None:
		print 'Create %s fail, it has exists'%title
	if not os.path.exists(os.path.join(POST_PATH, date)):
		os.makedirs(os.path.join(POST_PATH, date))
	with open(os.path.join(POST_PATH, date, '%s.md'%title), 'w') as post:
		post.write('<!-- default -->')
		with open(INDEX, 'r+') as idfile:
			idx=int(idfile.readline()[1:])
			id_info=['#%d'%(idx+1),]
			for line in idfile:
				id_info.append(line.rstrip())
			id_info.append(' %d %s %s' % (idx, title, date))
			idfile.seek(0)
			idfile.truncate(0)
			idfile.write('\n'.join(id_info))


def edit(title, date):
	"""
	edit blog
	:param tilte: blog title
	:param date: blog created/modified date
	:return
	"""
	print 'edit ', title, ' ', date
	
	
def remove(title, date):
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
		'\tclear: clear generated files',
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
	elif len(sys.argv)>=2 and sys.argv[1] == 'clear':
		clear()
	elif len(sys.argv)>=2 and (sys.argv[1] != 'init' and sys.argv[1] != 'clear'):
		action = sys.argv[1]
		title = None
		date = None
		if len(sys.argv)>=3:
			title = sys.argv[2]
		if len(sys.argv)>=4:
			date = sys.argv[3]
		try:
			datetime.datetime.strptime(date, DATE_FMT)
		except (ValueError, TypeError) :
			date = None
		try:
			globals()[action](title, date)
		except KeyError:
			usage()
	else:
		usage()

	
