while True:
    try:
        for _ in range(int(input())):
        	a,b,c = map(int,input().split())
        
        	TotalSum = a+2*b+3*c
        
        	if  TotalSum%2 ==1:
        		print("NO")
        	else:
        		Possible=False
        		HalfSum = TotalSum//2
        		icurr = 0
        		for i in range(min(c,HalfSum//3),-1,-1):
        			RemainingSum = HalfSum - 3*i
        			curr =0
        			for j in range(min(b,RemainingSum//2),-1,-1):
        				if (RemainingSum - 2*j) <= a:
        					Possible = True
        				curr+=1
        				if curr == 3:
        					break
        			icurr+=1
        			if icurr == 3:
        				break
        		print("YES" if Possible else "NO")
    except:
        break
