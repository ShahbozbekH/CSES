import sys

if __name__ == "__main__":
	#inFile = sys.argv[1]
	#f = open(inFile)
	#fread = int(f.readline())
	fread = int(input())
	ans = []
	while (fread != 1):
		ans.append(fread)
		if (fread%2 == 0):
			fread = int(fread/2)
			continue
		fread = (fread*3)+1
	ans.append(1)
	print(*ans)
