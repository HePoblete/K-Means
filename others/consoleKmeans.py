import random
import math
import sys

inFile = sys.argv[1]
#outFile = open("values_output.txt","w")
NUM_CLUSTERS = (int(sys.argv[2]))

TOTAL_DATA = 0
LOWEST_SAMPLE_POINT = 0
HIGHEST_SAMPLE_POINT = 2
BIG_NUMBER = math.pow(10, 10)

with open(inFile) as f:
	SAMPLES =[]
	for line in f:
		line = line.split()
		TOTAL_DATA += 1
		if line:
			line = [int(i) for i in line]
			SAMPLES.append(line)

if NUM_CLUSTERS > TOTAL_DATA:
	print
	print "Number of Clusters cannot be greater than number of DataSets"
	print "Please try again"
	exit()

RAND_SAMPLE = random.sample(range(TOTAL_DATA), NUM_CLUSTERS)

data = []
centroids = []

class DataPoint:
	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def set_x(self, x):
		self.x = x
	
	def get_x(self):
		return self.x
	
	def set_y(self, y):
		self.y = y
	
	def get_y(self):
		return self.y

	def set_cluster(self, clusterNumber):
		self.clusterNumber = clusterNumber

	def get_cluster(self):
		return self.clusterNumber

class Centroid:
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def set_x(self, x):
		self.x = x

	def get_x(self):
		return self.x

	def set_y(self, y):
		self.y = y

	def get_y(self):
		return self.y

def initialize_centroids():

	for i in range(NUM_CLUSTERS):	
		centroids.append(Centroid(SAMPLES[RAND_SAMPLE[i]][0], SAMPLES[RAND_SAMPLE[i]][1]))
	print
	print("DataSets chosen as Centriods were:")
	for i in range(NUM_CLUSTERS):
		print(centroids[i].get_x(), centroids[i].get_y())
	print  
	return

def initialize_datapoints():
	for i in range(TOTAL_DATA):
		newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1])
		
		for j in range(NUM_CLUSTERS):
			if(i == RAND_SAMPLE[j]):
				newPoint.set_cluster(j)
			else:
				newPoint.set_cluster(None)
		
		data.append(newPoint)

	return

def get_distance(dataPointX, dataPointY, centroidX, centroidY):
	return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))

def recalculate_centroids():
	totalX = 0
	totalY = 0
	totalInCluster = 0
	
	for j in range(NUM_CLUSTERS):
		for k in range(len(data)):
			if(data[k].get_cluster() == j):
				totalX += data[k].get_x()
				totalY += data[k].get_y()
				totalInCluster += 1

		if(totalInCluster > 0):
			centroids[j].set_x(totalX / totalInCluster)
			centroids[j].set_y(totalY / totalInCluster)

	return

def update_clusters():
	isStillMoving = 0

	for i in range(TOTAL_DATA):
		bestMinimum = BIG_NUMBER
		currentCluster = 0

		for j in range(NUM_CLUSTERS):
			distance = get_distance(data[i].get_x(), data[i].get_y(), centroids[j].get_x(), centroids[j].get_y())
			if(distance < bestMinimum):
				bestMinimum = distance
				currentCluster = j

		data[i].set_cluster(currentCluster)

		if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
			data[i].set_cluster(currentCluster)
			isStrillMoving = 1
	
	return isStillMoving

def perform_kmeans():
	isStillMoving = 1
	
	initialize_centroids()
	
	initialize_datapoints()

	while(isStillMoving):
		recalculate_centroids()
		isStillMoving = update_clusters()

	return

def print_results():
	for i in range(NUM_CLUSTERS):
		print "In cluster", i,":"
		for j in range(TOTAL_DATA):
			if(data[j].get_cluster() == i):
				print(data[j].get_x(), data[j].get_y())
		print  
	return

perform_kmeans()
print_results()
#outFile.close()

