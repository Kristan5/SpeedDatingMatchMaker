class Person:
    def __init__(self, id, name, age, gender, relationship, preference): 
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.relationship = relationship
        self.preference = preference
        self.matched_status = False
        self.past_dates = set()
