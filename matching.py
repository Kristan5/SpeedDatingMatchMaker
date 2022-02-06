import csv

from cv2 import AgastFeatureDetector
from Person import *

class SpeedDating:
	candidates = {}

	def readCSV(self):
		with open("candidates.csv", 'r') as t1:
			candidates_csv = t1.readlines()
			for row in candidates_csv:
				candidate_attributes = row.split(",")
				preference = self.preference_builder(candidate_attributes[11])
				candidate = Person(candidate_attributes[0],
								   candidate_attributes[2],
								   candidate_attributes[6],
								   candidate_attributes[7],
								   candidate_attributes[10],
								   preference)
				self.candidates[candidate_attributes[0]] = candidate
				# self.candidates.append(candidate)
		self.candidates.pop("id")

	def preference_builder(self, preference): 
		if preference == "Both":
			return ["Men", "Women"]
		return [preference]

	# Checks: 
	# 	- i not in j past dates
	# 	- i gender in j preference
	# 	- i age == j age
	def match(self):
		for i in self.candidates: 
			for j in self.candidates: 
				i = self.candidates.get(i)
				j = self.candidates.get(j)
				if j not in i.past_dates and i.age == j.age:
					i.past_dates.add(j)
					j.past_dates.add(i)
					print(f"{i.name} : {j.name}")
					# self.candidates.pop(i.id)
					# self.candidates.pop(j.id)



if __name__ == '__main__':
	s = SpeedDating()
	s.readCSV()
	s.match()