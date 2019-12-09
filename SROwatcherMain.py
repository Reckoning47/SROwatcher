"""
	Chris Cooper
	EIND 422 Intro to Simulation
	SROwatcher is a python utility to assist collecting data at the SRO coffee shop at Montana State University Bozeman
"""

import time
import csv

# Student class
class Student:

	def __init__(self, description, id):
		# create student with a description (to help humans keep track) and arrivalTime (automatically used on creation)
		self.description = description
		self.id = id
		self.arrivalTime = time.time()
		self.orderTime = 0.0
		self.waitTime = 0.0
		self.departureTime = 0.0
		self.currentPhase = 1
		self.stop = False

	def setArrivalTime(self, newTime):
		self.arrivalTime = newTime

	def setOrderTime(self, newTime):
		self.orderTime = newTime

	def setWaitTime(self, newTime):
		self.waitTime = newTime


	# TODO DEFINE PROCESS LOGIC INSIDE HERE
	# need to do update table with times, etc...use dictionary or data frame (dict maybe better)
	# TODO define queue class or queue inside of this class
	def nextPhase(self):
		print("Processing student to next phase: %s" % (self.description))
		temp = self.currentPhase
		if(temp == 1):
			print("Entity %s begins ordering\n" % self.description)
			time_dif = time.time() - self.arrivalTime
			self.orderTime = self.arrivalTime + time_dif
			self.currentPhase += 1
		if(temp == 2):
			print("Entity %s waits for order\n" % self.description)
			time_dif = time.time() - self.orderTime
			self.waitTime = self.orderTime + time_dif
			self.currentPhase += 1
		if(temp == 3):
			print("Entity %s has received their order\n" % self.description)
			time_dif = time.time() - self.waitTime
			self.departureTime = self.waitTime + time_dif
			self.currentPhase += 1
			self.stop = True

	def printInfo(self):
		return str(self.id) + ": " + self.description


if __name__ == '__main__':
	entities = {}
	# myCreation = Student("kakis")
	print("Starting application...\n")
	print("Please enter description for first student:")
	current_id = 1
	max_id = current_id

	# test = time.time()
	# print(test)
	# print(time.time())
	# time.sleep(8)
	# print(time.time())
	# print(test + time.time())
	# test2 = test + time.ctime()[11:20]
	# print(test2)


	while(True):
		print("Please input from the following menu: Press 0 to exit")
		user_input = input()
		if(user_input == '0'):
			break
		else:
			if user_input.isdigit():
				if int(user_input) < max_id:
					if int(user_input) in entities:
						entities[int(user_input)].nextPhase()
					else:
						print("input out of bounds try again")


			else:
				new_student = Student(user_input, current_id)
				entities[current_id] = new_student
				current_id += 1
				if(max_id < current_id):
					max_id = current_id

			for entity in entities:
				if(entities[entity].stop == False):
					print(entities[entity].printInfo())


	print("exiting...")
	# for entity in entities:
	# 	print("Entity: %s \n" % entities[entity].description)
	# 	print("\tArrival time: %s \n"
	# 		  "\tOrder time: %s \n"
	# 		  "\tWait start time: %s \n"
	# 		  "\tDeparture time: %s \n" % (entities[entity].arrivalTime, entities[entity].orderTime,
	# 		  								entities[entity].waitTime, entities[entity].departureTime))



	with open('output.csv', 'w', newline='') as outfile:
		outputWriter = csv.writer(outfile)
		# outputWriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		outputWriter.writerow(['Entity', 'Arrival Time', 'Order Time', 'Wait Start Time', 'Departure Time'])
		for entity in entities:
			outputWriter.writerow([entities[entity].description, entities[entity].arrivalTime,
								  entities[entity].orderTime, entities[entity].waitTime,
								  entities[entity].departureTime] )

