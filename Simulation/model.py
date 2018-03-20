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
        # of these positions and "move" throughout the simulation.
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
            student = Student(ideology, diplomacy, index)
            self.grid[index] = student
            index += 1

        for n in range(num_speakers):
            ideology = np.random.normal(expected_student_speaker_ideology, student_speaker_ideology_std_deviation)
            # The diplomacy score must be non-negative
            diplomacy = abs(np.random.normal(expected_speaker_diplomacy, speaker_diplomacy_std_deviation))
            speaker = Speaker(ideology, diplomacy, index)
            self.grid[index] = speaker
            index += 1
        # print(self.grid)
        # Now to 'shuffle' the grid so that some random initial positioning of the agents takes place
        np.random.shuffle(self.grid)
        # print(self.grid)
        self.grid = np.mat(self.grid).reshape(GRID_SIZE, GRID_SIZE)
        # print(self.grid)
        # Now iterate over the entire grid, and search for position of students, speakers
        self.students = list()
        self.speakers = list()
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if isinstance(self.grid[r,c], Student):
                    self.grid[r,c].set_position(r, c)
                    # Add found student to array of students that will be used later on to iterate over?
                    self.students.append(self.grid[r,c])
                    # print("Found student at row: %d, column: %d, x: %d, y: %d, uid: %s" % \
                    #     (r, c, self.grid[r,c].x, self.grid[r,c].y, self.grid[r,c].uid))
                if isinstance(self.grid[r,c], Speaker):
                    self.grid[r,c].set_position(r, c)
                    # Add found speaker to array of speakers that will be used later on to iterate over?
                    self.speakers.append(self.grid[r,c])
                    # print("Found speaker at row: %d, column: %d, x: %d, y: %d, uid: %s" % \
                    #     (r, c, self.grid[r,c].x, self.grid[r,c].y, self.grid[r,c].uid))
        # print(self.students)
        # print(self.speakers)

    def run_model(self):
        for t in range(1):
            print("At timestep %d" % (t))
            self.step()

    # So within each step can have the iteration to check for the interactions and then 
    # another iteration to check for the steps to take
    def step(self):
        # The first iteration to account for whatever interactions have occurred, and 
        # the second iteration to update change in location (if such a change can occur) for a given agent.
        # So first, go over speakers, and then look into iterating over students
        for speaker in self.speakers:
            print("at speaker %s" % (speaker.uid))
            for student in self.find_students(speaker.x, speaker.y, self.speaker_range):
                speaker.interacts_with(student)

    def find_students(self, center_x, center_y, max_range):
        # Returns a list of all people who are at most max_range units away
        # from position (center_x, center_y)
        x_min = max(center_x - max_range, 0)
        y_min = max(center_y - max_range, 0)
        x_max = min(center_x + max_range + 1, GRID_SIZE)
        y_max = min(center_y + max_range + 1, GRID_SIZE)
        # Using a set so that duplicate items are not added
        found_students = set()
        for r in range(x_min, x_max):
            for c in range(y_min, y_max):
                if isinstance(self.grid[r,c], Student):
                    print("found student %s at r: %d, c: %d" % (self.grid[r,c].uid, r, c))
                    found_students.add(self.grid[r,c])
        print("students found:", found_students)
        return found_students
