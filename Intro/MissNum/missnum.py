#import sys

if __name__ == "__main__":
	#inFile = sys.argv[1]
	#f = open(inFile)
	n = int(input())
	setLine = {int(x) for x in input().split()}
	for i in range (1, n+1):
		try:
			setLine.remove(i)
		except:
			print(i)


