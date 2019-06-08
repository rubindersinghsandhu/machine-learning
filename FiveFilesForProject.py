import random as r
import string as s
import os, sys, time, threading, multiprocessing

numberOfCores=multiprocessing.cpu_count()

def task(cmd):
   	# create file of cmd*GB file
	randstr=''.join(r.sample(s.ascii_letters,r.randint(5,10)))
	randsize=int(cmd)*1048576*1024
	print(randsize)
	sloc="D:\\computer\\PROJECTS\\summer 2019\\randomfiles\\%s"%(randstr)
	fp=open(sloc,'w')
	statinfo = os.stat(sloc)
	while(statinfo.st_size<randsize):	
		statinfo = os.stat(sloc)
		randstr=[''.join(r.sample(s.ascii_letters,1))*1024]
		fp.write(''.join(randstr))
	return

# Run Multiple Thread

for i in range(5):
    cmd=str(i+1)
    msg="...Thread %s start...."%(cmd)
    print(msg)
    t = threading.Thread(target=task , args=(cmd,))
    t.start()
    while True:
        if threading.activeCount()-1 <= numberOfCores:
            break
        time.sleep(1)

# Waiting to finish the thread
while True:
  if threading.activeCount() == 1:
    break
  time.sleep(1)
  print ("Thread Left ... ",threading.activeCount() - 1)

print("\n...All Thread ends....")