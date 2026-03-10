#import sys

if __name__ == "__main__":
	#inFile = sys.argv[1]
	#f = open(inFile)
	fread = input()
	largest = 0
	curr = {
		"letter" : None,
		"size" : 0,
	}
	for i in fread:
		if curr["letter"] is None:
			curr["letter"] = i
			curr["size"] = 1
			largest = 1
			continue
		if curr["letter"] is i:
			curr["size"] += 1
			if curr["size"] > largest:
				largest = curr["size"]
			continue
		if curr["size"] > largest:
			largest = curr["size"]
		curr["letter"] = i
		curr["size"] = 1
	print(largest)
