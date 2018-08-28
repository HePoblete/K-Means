import random						#import to randomize initialize centroids
import math 						#import to use pow
import sys						#import to deal with file I/O

inFile = sys.argv[1]					#read input file name  from console input
outFile = open("values_output.txt","w")			#create output file
NUM_CLUSTERS = (int(sys.argv[2]))			#read number of clusters desired from console input

TOTAL_DATA = 0						#initalization of value that holds the total number of data sets
BIG_NUMBER = math.pow(10, 10)

with open(inFile) as f:					#read all the datasets into program
	SAMPLES =[]
	for line in f:
		line = line.split()
		TOTAL_DATA += 1				#increment number of data sets
		if line:
			line = [int(i) for i in line]
			SAMPLES.append(line)

if NUM_CLUSTERS > TOTAL_DATA:				#input validation to make sure number of clusters is smaller than
	print						#number of datasets
	print "Number of Clusters cannot be greater than number of DataSets"
	print "Please try again"
	exit()

RAND_SAMPLE = random.sample(range(TOTAL_DATA), NUM_CLUSTERS)	#choosing the random datasets to be the first centroids

data = []
centroids = []

class DataPoint:					#creating class for Datapoints
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

class Centroid:						#creating class for centroids
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

def initialize_centroids():				#initializing the first centroids from the randomized
							#datasets selected above
	for i in range(NUM_CLUSTERS):	
		centroids.append(Centroid(SAMPLES[RAND_SAMPLE[i]][0], SAMPLES[RAND_SAMPLE[i]][1]))
	#outFile.write("DataSets chosen as Centriods were:  \n")
	#for i in range(NUM_CLUSTERS):
	#	outFile.write("[")
	#	chosenCents = (str(centroids[i].get_x()), ",",  str(centroids[i].get_y()))
	#	for j in range(len(chosenCents)):
	#		outFile.write(chosenCents[j])
			
	#	outFile.write("]\n")	
			
	#outFile.write("\n")  
	return

def initialize_datapoints():				#initializing the datapoints and assigning the centroids to a cluster
	for i in range(TOTAL_DATA):
		newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1])
		
		for j in range(NUM_CLUSTERS):
			if(i == RAND_SAMPLE[j]):
				newPoint.set_cluster(j)
			else:
				newPoint.set_cluster(None)
		
		data.append(newPoint)

	return

def get_distance(dataPointX, dataPointY, centroidX, centroidY):	#function to get distance between centroid and datapoint
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
		outFile.write("In cluster ")
		outFile.write(str(i))
		outFile.write(":\n")
		for j in range(TOTAL_DATA):
			if(data[j].get_cluster() == i):
				outFile.write("[")
				dataSets = (str(data[j].get_x()),"," ,str( data[j].get_y()))
				for k in range(len(dataSets)):
					outFile.write(dataSets[k])
				outFile.write("]\n")
		outFile.write("\n")  
	return

def print_fileout():
	#for i in range(TOTAL_DATA):
	#	print (data[i].get_x(), data[i].get_y(), data[i].get_cluster())

	for i in range(TOTAL_DATA):
		outFile.write(str(data[i].get_x()))
		outFile.write(" ")
		outFile.write(str(data[i].get_y()))
		outFile.write(" ")
		outFile.write(str(data[i].get_cluster()))
		outFile.write("\n")
		
perform_kmeans()
#print_results()
print_fileout()
outFile.close()

