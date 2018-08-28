import random
import sys

totalData = 5
clusterNum = int(sys.argv[1])

data = random.sample(range(totalData), clusterNum)

for i in range(clusterNum):
	print data[i]



