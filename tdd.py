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
	if len(b)>0:
		return a+' ma kota i '+b
	return a+' ma kota'

def f5(a,b=1):
	c=[]
	if a>0:
		for i in range(0,a,b):
			c.append(i)
	return c

def f6(a,b):
	c=''
	for i in range(0,a):
		c+='*'
	return c	

def f7(a):
	return 0
