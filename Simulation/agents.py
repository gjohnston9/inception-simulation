class Speaker:
    def __init__(self, ideology, diplomacy, uid):
        self.x = None
        self.y = None
        self.ideology = max(-100, min(100, ideology))
        self.diplomacy = max(0, min(100, diplomacy))
        self.uid = "Speaker_" + str(uid + 1)

    def interacts_with(self, student):
        pass
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
        self.has_interacted = true
        # TODO

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.ideology)

    def __repr__(self):
        return "Student: ({},{},{})".format(self.x, self.y, self.ideology)

