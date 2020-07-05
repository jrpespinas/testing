class Person:
    def __init__(
            self, fname, mname, lname,
            age, gender, bday,
            degree, occupation, hobbies
    ):
        self.first_name = fname
        self.middle_name = mname
        self.last_name = lname
        self.age = age
        self.gender = gender
        self.birthday = bday
        self.degree = degree
        self.occupation = occupation
        self.hobbies = hobbies

    def display_attributes(self):
        return self.first_name, self.middle_name, self.last_name, \
            self.age, self.gender, self.birthday, self.degree, \
            self.occupation, self.hobbies
