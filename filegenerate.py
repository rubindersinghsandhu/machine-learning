import random as r
import string as s
lenval=['10','11','12','13','14','15','16','17','18','19','20']
fp=open('sampledata.csv','w')
for i in range (1,1001):
	randstr=r.sample(s.ascii_letters,int(''.join(r.sample(lenval,1))))
	strlen=len(randstr)
	if(strlen%2==0):
		op='+'
	else:
		op='-'
	fp.write(str(i)+','+''.join(randstr)+','+op+'\n')
fp.close()
print('Done')

	