import math

def find_agreement(abs_difference, y_intercept=5, slope_factor=1, vertical_shift=1):
    # slope_factor should be > 0
    abs_difference = abs_difference / 20
    return (2 / (1 + math.exp(slope_factor*(abs_difference - y_intercept)))) - vertical_shift

class Speaker:
    def __init__(self, ideology, diplomacy, uid):
        self.x = None
        self.y = None
        self.ideology = max(-100, min(100, ideology))
        self.diplomacy = max(0, min(100, diplomacy))
        self.uid = "Speaker_" + str(uid + 1)

    def interacts_with(self, student):
        # print("student's initial ideology: {}".format(student.ideology))
        abs_difference = abs(self.ideology - student.ideology)
        # print("abs_difference: {}".format(abs_difference))
        agreement_score = find_agreement(abs_difference)
        if (self.ideology < student.ideology):
            agreement_score *= -1

        student.ideology += agreement_score
        # print("student's ideology after speaker interaction: {}".format(student.ideology))
        if student.ideology < -100 :
            student.ideology = -100
        if student.ideology > 100 :
            student.ideology = 100

        # print("in interacts with, student's position: (%d, %d), speaker's position: (%d, %d)" % \
            # (student.x, student.y, self.x, self.y))
        # print("in interacts with, student's ideology: %f, diplomacy: %f, speaker's ideology: %f,\
# speaker's diplomacy: %f" % (student.ideology, student.diplomacy, self.ideology, self.diplomacy))
        # if student.ideology < -3 and self.ideology > 3

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.ideology)

    def __repr__(self):
        return "Speaker: ({},{},{})".format(self.x, self.y, self.ideology)

class Student:
    def __init__(self, ideology, diplomacy, uid):
        self.x = None
        self.y = None
        self.ideology = max(-100, min(100, ideology))
        self.diplomacy = max(0, min(100, diplomacy))
        self.uid = "Student_" + str(uid + 1)

    def interacts_with(self, student):
        # print("student's initial ideology: {}".format(student.ideology))
        abs_difference = abs(self.ideology - student.ideology)
        # print("abs_difference: {}".format(abs_difference))
        agreement_score = find_agreement(abs_difference)
    
        # each student will move towards the mean
        self_change = agreement_score / 2
        other_change = agreement_score / 2
        if (self.ideology < student.ideology):
            other_change *= -1
        else:
            self_change *= -1

        self.ideology += self_change
        student.ideology += other_change
        # print("student's ideology after speaker interaction: {}".format(student.ideology))
        for s in (self, student):
            if s.ideology < -100 :
                s.ideology = -100
            if s.ideology > 100 :
                s.ideology = 100

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.ideology)

    def __repr__(self):
        return "Student: ({},{},{})".format(self.x, self.y, self.ideology)