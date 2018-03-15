from agents import Speaker, Student

import random

GRID_SIZE = 100

class Model:
    def __init__(self, num_students, num_speakers, speaker_range, ideology_variance, diplomacy_variance):
        # Right now this is a square grid where students are placed randomly.
        # If we want to specifically model Skiles walkway, then we can look at using
        # a rectangular grid with speakers placed near the bottom and top.
        self.student_grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.speakers = [] # Speakers are stationary and have their own x and y attributes
        self.speaker_range = speaker_range

        for n in range(num_students):
            x = random.randrange(GRID_SIZE)
            y = random.randrange(GRID_SIZE)
            student = Student(ideology_variance, diplomacy_variance)
            self.student_grid[x][y].append(student)
        
        for n in range(num_speakers):
            x = random.randrange(GRID_SIZE)
            y = random.randrange(GRID_SIZE)
            speaker = Speaker(ideology_variance, diplomacy_variance, x, y)
            self.speakers.append(speaker)

    def run_model(self):
        for t in range(500):
            self.step()

    def step(self):
        # First, model speaker-student interactions. Each speaker interacts with
        # all nearby student. Speaker_range defines the maximum distance at
        # which a speaker will interact with a student.
        for speaker in self.speakers:
            for student in self.find_students(speaker.x, speaker.y, self.speaker_range):
                speaker.interacts_with(student)

        # Next, model all student-student interactions. Each student interacts
        # with a random student on the same tile or on an adjacent tile.
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                students = self.student_grid[x][y] # list of all students at this position
                for student in students:
                    nearby_students = self.find_students(x, y, 1)
                    if len(nearby_students) != 1: # if 1, there are no students in range besides this person
                        other_person = random.choice(nearby_students)
                        while other_person is student: # avoid having someone interact with themselves
                            other_person = random.choice(nearby_students)
                        person.interacts_with(other_person)

    def find_students(self, center_x, center_y, max_range):
        # Returns a list of all people who are at most max_range units away
        # from position (center_x, center_y)
        x_min = max(center_x - max_range, 0)
        y_min = max(center_y - max_range, 0)
        x_max = min(center_x + max_range + 1, GRID_SIZE)
        y_max = min(center_y + max_range + 1, GRID_SIZE)
        students = []
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                students.extend(self.student_grid[x][y])
        return students
