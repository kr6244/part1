#!/usr/bin/python

import  os,commands

l=[]
dict={}
for  i  in  range(150)[140: ]  :
	
	x=os.system('arp -a ')
	print i
	if x == 0:
		l.append( "192.168.122."+str(i))
		ss=commands.getoutput( 'cat /proc/meminfo | head -1 | cut -d" " -f9')
		p=int(ss)		
		st="192.168.122."+str(i)
		dict[p]=st


a=dict.keys()
a.sort(reverse=True)

print dict.values()
print "your namenode is : "+dict[a[0]]


