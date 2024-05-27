n=int(input('n= '))
i=res=0
while n!=0:
	res=res+(n%10)*(2**i)
	n=n//10
	i+=1
print("n= ",res)
	