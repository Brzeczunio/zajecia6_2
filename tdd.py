#! /usr/bin/python

import re

def f1(a,b=0):
	return a*a+b

def f2(a):
	if not a:
		return 'BUUUUM'
	return a[0]

def f3(a):
	if a==1:
		return 'jeden'
	elif a==2:
		return 'dwa'
	elif a==3:
		return 'trzy' 
	return 'other'

def f4(a,b=''):
	if b:
		return '{0} ma kota i {1}'.format(a,b)
	return '{0} ma kota'.format(a)

def f5(a,b=1):
	c = range(a)
	return c[::b]

def f6(a,b):
	return a*b	

def f7(a):
	if re.match('^\d$',a):
		return 'cyfra'
	elif re.match('[0-9]+',a):
		return 'liczba'
	elif re.match('-[0-9]+',a):
		return 'liczba_ze_znakiem'
	elif re.match('^[A-Z][a-z]+.',a):
		return 'zdanie'
	elif re.match('[a-zA-Z]+',a):
		return 'slowo'
	elif re.match('<[a-zA-Z]+>',a):
		return 'tag poczatkowy'
	elif re.match('</[a-zA-Z]+>',a):
		return 'tag koncowy'

def f8(a,b):
	if re.search(a,b):
		return True
	return False

def f9(a,b):
	if a>0 and b>0:
		return 'dodatnie'
	elif a<0 and b<0:
		return 'ujemne'
	elif (a>0 and b<0) or (a<0 and b>0):
		return 'roznych znakow'
	elif a==0 or b==0:
		return 'jest zero'
	elif a==b:
		return 'rowne'

def f10(a,b):
	if a==b:
		return 'rowne'
	else:
		return 'rozne'
