import sys

inFile = sys.argv[1]
NUM_CLUSTERS = sys.argv[2]

with open(inFile) as f:
	SAMPLES =[]
	for line in f:
		line = line.split()
		if line:
			line = [int(i) for i in line]
			SAMPLES.append(line)

print SAMPLES
print "Number of clusters = ", NUM_CLUSTERS


