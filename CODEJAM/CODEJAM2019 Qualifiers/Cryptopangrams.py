primes=[]
prime=[]
def SieveOfEratosthenes(n):
	global primes
	global prime
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True) :
			for i in range(p * p, n+1, p) :
				prime[i] = False
		p += 1

	for p in range(2, n) :
		if prime[p] :
			primes.append(p)


for _ in range(int(input())):
	n,l = map(int,input().split())
	cipher = list(map(int,input().split()))
	SieveOfEratosthenes(n)
	first=cipher[0]
	found=False
	prime1=0
	prime2=0

	deciphers=[]

	for div in primes :
		if (first/div) == first//div :
			prime2 = first // div
			prime1 = div
			found =True
			break


	deciphers.extend([prime1,prime2])
	
	for i in range(1,l) :
		prevprime1 = deciphers[-1]
		prevprime2 = deciphers[-2]

		if cipher[i] % prevprime1 == 0 :
			deciphers.append(cipher[i] // prevprime1)
		elif cipher[i] % prevprime2 == 0 :
			len_decipher=len(deciphers)
			temp=deciphers[::2]
			deciphers[::2]=deciphers[1::2]
			deciphers[1::2]=temp
			deciphers.append(cipher[i] // prevprime2)
	
	#print(sorted(deciphers),sorted(list(set(deciphers))),cnt,sep="\n")

	extract_letters=sorted(list(set(deciphers)))
	#print(deciphers,extract_letters)
	output=''
	for ciph in deciphers :
		ind=extract_letters.index(ciph)			#search(extract_letters,0,25,ciph)
		if ind>=0 :
			temp=ind+65
			temp=chr(temp)
			output+=temp
	
	print("Case #",_+1,":",sep="",end=" ")
	print(output)