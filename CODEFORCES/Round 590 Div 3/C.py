for _ in range(int(input())):
	n=int(input())
	pipes = [[int(i) for i in input().strip()] for i in range(2)]

	currenti,currentj=0,0


	maxIters = 0

	while True:
		#print("Iteration ",maxIters)
		#print(currenti,currentj,pipes[currenti][currentj])
		#print(pipes[currenti][currentj] in [3,4,5,6,7])
		if pipes[currenti][currentj] in [1,2]:
			#print("Main yaha hu")
			currentj+=1
		elif (pipes[currenti][currentj] in [3,4,5,6,7]) and (pipes[(currenti+1)%2][currentj] in [3,4,5,6,7]):
			#print("In here")
			currenti+=1
			currenti%=2

			currentj+=1

		maxIters+=1
		if currentj == n or maxIters>(2*n)+1:
			break
		#print(end="\n")
	if currenti==1 and currentj == n:
		print("YES")
	else:
		print("NO")