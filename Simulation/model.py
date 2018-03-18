from agents import Speaker, Student

import numpy as np
import random
import math 
import sys

GRID_SIZE = 10

# Updating the model to step over each agent in the simulation rather than each square
# So the model will have a 2D array that it uses to keep track of each agent in the simulation.
# For the first loop over the agents and update the interactions. 
# For the second loop, update the position of each of the agents
class Model:
    def __init__(self, num_students, num_speakers, speaker_range, ideology_variance, diplomacy_variance):
        # Right now this is a square grid where students are placed randomly.
        # If we want to specifically model Skiles walkway, then we can look at using
        # a rectangular grid with speakers placed near the bottom and top.
        # self.student_grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # Check to ensure number of students is within model limit
        num_students_limit = math.ceil(GRID_SIZE / 2)
        if num_students > num_students_limit:
            print("The number of students, %d, entered for simulation exceeds model limit, %d. \
Please enter a number less than or equal to %d." % (num_students, num_students_limit, math.ceil(GRID_SIZE / 2)))
            sys.exit()

        # Check to ensure number of speakers is within model limit
        num_speakers_limit = math.ceil(GRID_SIZE / 4)
        if num_speakers > num_speakers_limit:
            print("The number of speakers, %d, entered for simulation exceeds model limit, %d. \
Please enter a number less than or equal to %d." % (num_speakers, num_speakers_limit, math.ceil(GRID_SIZE / 4)))
            sys.exit()

        # Initializes a square array where each element is None. The agent objects will take the place
        # of these positions and "move" throughout the simulation
        # self.grid = [[None for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
        # Seems like it might be nice to experiment on the number of speakers in the simulation
        # self.speakers = [] # Speakers are stationary and have their own x and y attributes
        self.grid = [ None ] * (GRID_SIZE * GRID_SIZE)
        self.speaker_range = speaker_range

        # Look into drawing ideology and diplomacy scores from a normal distribution
        expected_student_speaker_ideology, student_speaker_ideology_std_deviation = 0, 3
        expected_student_diplomacy, student_diplomacy_std_deviation = 0, 1
        expected_speaker_diplomacy, speaker_diplomacy_std_deviation = 0, 2
        index = 0
        for n in range(num_students):
            # The ideology can be positive or negative
            ideology = np.random.normal(expected_student_speaker_ideology, student_speaker_ideology_std_deviation)
            # The diplomacy score must be non-negative
            diplomacy = abs(np.random.normal(expected_student_diplomacy, student_diplomacy_std_deviation))
            student = Student(ideology, diplomacy)
            self.grid[index] = student
            index += 1

        for n in range(num_speakers):
            ideology = np.random.normal(expected_student_speaker_ideology, student_speaker_ideology_std_deviation)
            # The diplomacy score must be non-negative
            diplomacy = abs(np.random.normal(expected_speaker_diplomacy, speaker_diplomacy_std_deviation))
            speaker = Speaker(ideology, diplomacy)
            self.grid[index] = speaker
            index += 1
        # print(self.grid)
        # Now to 'shuffle' the grid so that some random initial positioning of the agents takes place
        np.random.shuffle(self.grid)
        # print(self.grid)
        self.grid = np.mat(self.grid).reshape(GRID_SIZE, GRID_SIZE)
        # print(self.grid)
        # Now iterate over the entire grid, and search for position of students, speakers
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if isinstance(self.grid[r,c], Student):
                    self.grid[r,c].set_position(r, c)
                    # print("row: %d, column: %d, x: %d, y: %d" % (r, c, self.grid[r,c].x, self.grid[r,c].y))


        # for n in range(num_students):
        #     # The ideology can be positive or negative
        #     ideology = np.random.normal(expected_ideology, ideology_std_deviation)
        #     diplomacy = abs(np.random.normal(expected_diplomacy, diplomacy_std_deviation))
        #     student = Student(ideology, diplomacy)
        #     self.grid[index] = student
        #     # x = random.randrange(GRID_SIZE)
        #     # y = random.randrange(GRID_SIZE)
        #     # student = Student(ideology_variance, diplomacy_variance)
        #     # self.student_grid[x][y].append(student)

        # for n in range(num_speakers):
        #     x = random.randrange(GRID_SIZE)
        #     y = random.randrange(GRID_SIZE)
        #     speaker = Speaker(ideology_variance, diplomacy_variance, x, y)
        #     self.speakers.append(speaker)

    def run_model(self):
        for t in range(500):
            self.step()

    # So within each step can have the iteration to check for the interactions and then 
    # another iteration to check for the steps to take
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
