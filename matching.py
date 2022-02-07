"""
TODO: 
- Somethings wrong with preference matching
"""
import csv
from Person import *

class SpeedDating:
	# Candidates hashmap
	candidates = {}
	# End matches array of 2 tuples
	matches = []

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
		self.candidates.pop("id")

	def preference_builder(self, preference): 
		if preference == "Both":
			return ["Men", "Women"]
		return [preference]

	def valid_preferenece(self, person1, person2, recur):
		for i in person1.preference:
			# if recur and i == person2.gender and self.valid_preferenece(person2, person1, False):
				# return True
			print("i: ", i, ": person2.gender: ", person2.gender)
			if i == person2.gender: 
				return True
		return False
		# for i in person1.preference: 
		# 	if i in person2.preference: 
		# 		print("Valid preference: ", person1.name, " : ", person2.name)
		# 		return True
		# return False

	def valid_age(self, person1, person2):
		if person1.age == person2.age: return True
		return False

	def valid_new_date(self, person1, person2):
		if person2 not in person1.past_dates: return True
		return False

	def make_match(self, person1, person2):
		person1.past_dates.add(person2)
		person2.past_dates.add(person1)
		person1.matched_status = True
		person2.matched_status = True
		self.matches.append([person1.name, person2.name])

	def unmatched_toString(self): 
		print("\nUnmatched:")
		for key, value in self.candidates.items():
			if not value.matched_status: 
				print(value.name)
	
	def matched_toString(self): 
		print("\nMatched:")
		for i in s.matches: 
			print(i)
	
	# Checks: 
	# 	- i not in j past dates
	# 	- i gender in j preference
	# 	- i age == j age
	def match(self):
		for p1_key, person1 in self.candidates.items(): 
			for p2_key, person2 in self.candidates.items(): 
				if person2.matched_status or person1 == person2: continue
				valid_preference = self.valid_preferenece(person1, person2, True)
				valid_age = self.valid_age(person1, person2)
				valid_age = self.valid_age(person1, person2)
				valid_new_date = self.valid_new_date(person1, person2)
				if valid_preference and valid_new_date and valid_age:
					self.make_match(person1, person2)
					break



if __name__ == '__main__':
	s = SpeedDating()
	s.readCSV()
	s.match()
	s.matched_toString()
	s.unmatched_toString()

	# for key in s.candidates.keys():
		# print(i[1].name)
		# print(key)