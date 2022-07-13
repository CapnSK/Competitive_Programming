'''
	This is the code for convex hull. 
	It outputs the points on the border of hull in clockwise order starting from bottom left point.
'''

class Point:
	def __init__(self,x:int,y:int):
		self.x = x
		self.y = y

	def __lt__(self,P1):
		if self.x == P1.x:
			return self.y<P1.y
		return self.x<P1.x

def cw(A:Point,B:Point,C:Point):
	return A.x*(C.y-B.y) + B.x*(A.y-C.y) + C.x*(B.y-A.y) > 0

def ccw(A:Point,B:Point,C:Point):
	return A.x*(C.y-B.y) + B.x*(A.y-C.y) + C.x*(B.y-A.y) < 0

def collinear(A:Point,B:Point,C:Point):
	return A.x*(B.y-C.y) + B.x*(C.y-A.y) + C.x*(A.y-B.y) == 0

def Convex_Hull(Points:Point,n:int,debug:bool):
	Hull_Points = {}
	Points.sort()
	P1,P2 = Points[0],Points[-1]
	UP,DOWN = [P1],[P1]

	for i in range(1,n):
		Pi = Points[i]
		if i==n-1 or not ccw(P1,Pi,P2):
			while len(UP)>=2 and ccw(UP[-2],UP[-1],Pi):
				UP.pop()
			UP.append(Pi)
		if i==n-1 or not cw(P1,Pi,P2):
			while len(DOWN)>=2 and cw(DOWN[-2],DOWN[-1],Pi):
				DOWN.pop()
			DOWN.append(Pi)

	if debug:
		print("UP")
	for p in UP:
		if debug:
			print(p.x,p.y)
		if (p.x,p.y) not in Hull_Points:
			Hull_Points[(p.x,p.y)]=True

	if debug:
		print("DOWN")
	for p in DOWN[::-1]:
		if debug:
			print(p.x,p.y)
		if (p.x,p.y) not in Hull_Points:
			Hull_Points[(p.x,p.y)]=True	
	return list(Hull_Points.keys())



debug = eval(input("Debug?: "))
n = int(input("Enter number of points: "))
Points:Point = []
for i in range(n):
	x,y = map(int,input().split())
	Points.append(Point(x,y))
Convex_Points = Convex_Hull(Points,n,debug)


print("Convex Points in a clockwise order")
for p in Convex_Points:
	print(p[0],p[1])