#!/usr/bin/python -tt
import os
import time
import pycurl
import cStringIO
response = cStringIO.StringIO()
def getUserData():
    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'http://<<ip>>:8086/livestreamrecord/index.html') #set ip_address
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.VERBOSE, 0)
    c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
    c.setopt(pycurl.USERPWD, '<<user>>:<<password>>') #set username and password
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    c.close()

getUserData()
with open( "lists.txt", "r" ) as f:
#array = []
    newlines = []
    for line in f.readlines():
        if response.getvalue().find(line.rstrip()[:-2]) == -1:
            if line.rstrip()[-1:] == '1':
                print "NO_" + line
                os.system("/home/gleam/skcmd/skcmd.py chat <<name_skype_friend>> This is skynet say: " + line.rstrip()[:-2] + " is down.") #set name
                newlines.append(line.replace(':1', ':0'))
            else:
                newlines.append(line)
        else:
            if line.rstrip()[-1:] == '0':
                print "OK_" + line
                newlines.append(line.replace(':0', ':1'))
            else:
                newlines.append(line)
    #array.append( line )
#ins.close()
with open('lists.txt', 'w') as f:
    for line in newlines:
        f.write(line)
