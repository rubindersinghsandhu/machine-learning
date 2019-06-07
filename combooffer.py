import random as r
prod={'P1':64,'P2':88,'P3':152,'P4':93,'P5':100,'P6':50}
reqseq=[]
lran=300
uran=310
seqsum=0
for x in range(1000):
	randseq=[]
	templist=[]
	randseq.append(','.join(r.sample(prod.keys(),r.randint(1,6))))
	templist.append(randseq[0].split(','))
	for x in templist:
		for y in x:
			seqsum=seqsum+prod[y]
		if(seqsum<=uran and seqsum>=lran):
			reqseq.append(''.join(x))
	seqsum=0
print("Combo offers between {} and {} are ".format(lran,uran),reqseq)







	