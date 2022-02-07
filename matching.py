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
			for row in candidates_csv[1:-1]:
				candidate_attributes = row.split(",")
				candidates_attribuets_len = len(candidate_attributes)
				preference = self.preference_builder(candidate_attributes[candidates_attribuets_len-1])
				gender = self.gender_builder(candidate_attributes[7])
				candidate = Person(candidate_attributes[0],
								   candidate_attributes[2],
								   candidate_attributes[6],
								   gender,
								   candidate_attributes[candidates_attribuets_len-2],
								   preference)
				self.candidates[candidate_attributes[0]] = candidate

	def gender_builder(self, gender):
		men = {"men", "man", "male", "guy", "boy"}
		women = {"women", "woman", "female", "girl"}
		if self.format_gender(gender) in men: return "Men"
		if self.format_gender(gender) in women: return "Women"
		raise Exception("INVALID GENDER: ", gender)

	def format_gender(self, gender): 
		return ''.join(filter(str.isalnum, gender)).lower()

	def preference_builder(self, preference): 
		if preference == "Both\n": return ["Men", "Women"]
		if preference == "Men\n": return ["Men"]
		if preference == "Women\n": return ["Women"]
		return [preference]

	def valid_preferenece(self, person1, person2):
		person1_check = self.check_individual_preference(person1, person2)
		person2_check = self.check_individual_preference(person2, person1)
		if person1_check and person2_check: return True
		return False

	def check_individual_preference(self, person1, person2):
		for preference in person1.preference: 
			if person2.gender == preference:
				return True
		return False

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
	
	def candidates_toString(self): 
		for key, value in self.candidates.items(): 
			print("id: ", value.id)
			print("name: ", value.name)
			print("age: ", value.age)
			print("gender: ", value.gender)
			print("relationship: ", value.relationship)
			print("preference: ", value.preference, '\n')


	# Checks: 
	# 	- i not in j past dates
	# 	- i gender in j preference
	# 	- i age == j age
	def match(self):
		for p1_key, person1 in self.candidates.items(): 
			for p2_key, person2 in self.candidates.items(): 
				if person1.matched_status or person2.matched_status or person1 == person2: continue
				valid_preference = self.valid_preferenece(person1, person2)
				valid_age = self.valid_age(person1, person2)
				valid_new_date = self.valid_new_date(person1, person2)
				if valid_preference and valid_new_date and valid_age:
					self.make_match(person1, person2)
					break



if __name__ == '__main__':
	s = SpeedDating()
	s.readCSV()
	# s.candidates_toString()
	s.match()
	s.matched_toString()
	s.unmatched_toString()
