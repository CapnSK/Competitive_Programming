class Result(object):
	def __init__(self,mean,mode,median):
		self.a=mean
		self.b=median
		self.c=mode

def main():
	return 1,2,3

a,b,c=main()
print(a,b,c)