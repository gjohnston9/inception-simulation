class Speaker:
    def __init__(self, ideology_variance, diplomacy_variance, uid):
        self.x = None
        self.y = None
        self.ideology = ideology_variance
        self.diplomacy = diplomacy_variance
        self.uid = "Speaker_" + str(uid + 1)

    def interacts_with(self, student):
        print("in interacts with, student's position: (%d, %d), speaker's position: (%d, %d)" % \
            (student.x, student.y, self.x, self.y))
        print("in interacts with, student's ideology: %f, diplomacy: %f, speaker's ideology: %f,\
speaker's diplomacy: %f" % (student.ideology, student.diplomacy, self.ideology, self.diplomacy))
        # if student.ideology < -3 and self.ideology > 3

    def set_position(self, x, y):
        self.x = x
        self.y = y

class Student:
    def __init__(self, ideology_variance, diplomacy_variance, uid):
        self.x = None
        self.y = None
        self.ideology = ideology_variance
        self.diplomacy = diplomacy_variance
        self.uid = "Student_" + str(uid + 1)
        # TODO: use variances to initialize ideology and diplomacy levels

    def interacts_with(self, student):
        self.has_interacted = true
        # TODO

    def set_position(self, x, y):
        self.x = x
        self.y = y
