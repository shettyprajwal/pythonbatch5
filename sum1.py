def find_sum(n,num):
	i=0
	sum=0
	while i<n:
		sum=sum+num[i]
		i=i+1	
	
		
	print('the sum is {0}'.format(sum))
	

i=0
num=[]
print('enter  n')	
n=input()
print('enter' the list')
while i<n:
	r=input()
	i=i+1
	num.append(r)
find_sum(n,num)
