from agents import Speaker, Student

import numpy as np
import random
import math 
import os
import sys

GRID_SIZE = 10

# Updating the model to step over each agent in the simulation rather than each square
# So the model will have a 2D array that it uses to keep track of each agent in the simulation.
# For the first loop over the agents and update the interactions. 
# For the second loop, update the position of each of the agents
class Model:
    def __init__(
        self,
        experiment_name,
        population_density,
        students_to_speakers_ratio,
        speaker_range,

        expected_student_diplomacy,
        expected_speaker_diplomacy,
        expected_abs_student_ideology,
        expected_abs_speaker_ideology,

        student_diplomacy_std_deviation,
        speaker_diplomacy_std_deviation,
        student_ideology_std_deviation,
        speaker_ideology_std_deviation,
        random_seed=None):
        """
        (string) experiment_name: name of the experiment being run

        (float) population_density: percentage of tiles on the grid that will be filled; should be a float,
            between 0.05 and 0.95 (inclusive)
        (int) students_to_speakers_ratio: number of students for each speaker; should be an int between 20 and
            500 (inclusive)
        
        (int) speaker_range: maximum distance across which a speaker can communicate with a student
        (int) expected_student_diplomacy: expected value for student diplomacy; should be an int between 0 and 100 (exclusive)
        (int) expected_speaker_diplomacy: expected value for speaker diplomacy; should be an int  between 0 and 100 (exclusive)
        (int) expected_abs_student_ideology: expected absolute value for student ideology; should be an int between 0 and 100 (exclusive)
        (int) expected_abs_speaker_ideology: expected absolute value for speaker ideology; should be an int between 0 and 100 (exclusive)
        
        (int) student_diplomacy_std_deviation: standard deviation for student diplomacy; should be an int between 0 and 50 (exclusive)
        (int) speaker_diplomacy_std_deviation: standard deviation for speaker diplomacy; should be an int between 0 and 50 (exclusive)
        (int) student_ideology_std_deviation: standard deviation for student ideology; should be an int between 0 and 50 (exclusive)
        (int) speaker_ideology_std_deviation: standard deviation for speaker ideology; should be an int between 0 and 50 (exclusive)
        """
        num_tiles = GRID_SIZE ** 2
        assert 0.05 <=  population_density <= 0.95, "Population density was {}, should be between 0.05 and 0.95".format(population_density)
        assert students_to_speakers_ratio == int(students_to_speakers_ratio), "Students to speakers ratio was {}, should be a whole number".format(students_to_speakers_ratio)
        assert 20 <= students_to_speakers_ratio <= 500, "Students to speakers ratio was {}, should be between 20 and 500".format(students_to_speakers_ratio)
        num_people = int(population_density * num_tiles)
        num_speakers = int(num_people / (students_to_speakers_ratio + 1))
        num_students = num_people - num_speakers
        np.random.seed(random_seed)
        random.seed(random_seed)

        for val in (expected_student_diplomacy, expected_speaker_diplomacy, expected_abs_student_ideology, expected_abs_speaker_ideology):
            assert 0 < val < 100, "expected_student_diplomacy, expected_speaker_diplomacy, expected_abs_student_ideology, expected_abs_speaker_ideology "\
            "should all be between 0 and 100 (exclusive), but they are {}, {}, {}, and {}".format(
                expected_student_diplomacy, expected_speaker_diplomacy, expected_abs_student_ideology, expected_abs_speaker_ideology)

        for val in (student_diplomacy_std_deviation, speaker_diplomacy_std_deviation, student_ideology_std_deviation, speaker_ideology_std_deviation):
            assert 0 < val < 50, "student_diplomacy_std_deviation, speaker_diplomacy_std_deviation, student_ideology_std_deviation, speaker_ideology_std_deviation "\
            "should be between 0 and 50 (exclusive), but they are {}, {}, {}, and {}".format(
                student_diplomacy_std_deviation, speaker_diplomacy_std_deviation, student_ideology_std_deviation, speaker_ideology_std_deviation)

        self.expected_abs_student_ideology = expected_abs_student_ideology
        self.expected_abs_speaker_ideology = expected_abs_speaker_ideology
        self.speaker_range = speaker_range

        # Initializes a square array where each element is None. The agent objects will take the place
        # of these positions and "move" throughout the simulation.
        self.grid = [ None ] * (GRID_SIZE * GRID_SIZE)

        index = 0
        for n in range(num_students):
            # The ideology can be positive or negative
            ideology = np.random.normal(expected_abs_student_ideology, student_ideology_std_deviation)
            ideology *= random.choice([1, -1]) # flip sign with 50% probability
            # The diplomacy score must be non-negative
            diplomacy = abs(np.random.normal(expected_student_diplomacy, student_diplomacy_std_deviation))
            student = Student(ideology, diplomacy, index)
            self.grid[index] = student
            index += 1

        for n in range(num_speakers):
            ideology = np.random.normal(expected_abs_speaker_ideology, speaker_ideology_std_deviation)
            ideology *= random.choice([1, -1]) # flip sign with 50% probability
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

        self.log_filename = "_".join(map(str, [
            experiment_name,

            population_density,
            students_to_speakers_ratio,
            speaker_range,

            expected_student_diplomacy,
            expected_speaker_diplomacy,
            expected_abs_student_ideology,
            expected_abs_speaker_ideology,

            student_diplomacy_std_deviation,
            speaker_diplomacy_std_deviation,
            student_ideology_std_deviation,
            speaker_ideology_std_deviation,

            random_seed])) + ".vis"

        self.log_filename = os.path.join("..", "Logs", self.log_filename)

        with open(self.log_filename, "w") as f:
            f.write("width:{0}\nheight:{0}\n".format(GRID_SIZE))
            f.write("population_density:{}\n".format(population_density))
            f.write("students_to_speakers_ratio:{}\n".format(students_to_speakers_ratio))

            f.write("expected_student_diplomacy:{}\n".format(expected_student_diplomacy))
            f.write("expected_speaker_diplomacy:{}\n".format(expected_speaker_diplomacy))
            f.write("expected_abs_student_ideology:{}\n".format(expected_abs_student_ideology))
            f.write("expected_abs_speaker_ideology:{}\n".format(expected_abs_speaker_ideology))

            f.write("student_diplomacy_std_deviation:{}\n".format(student_diplomacy_std_deviation))
            f.write("speaker_diplomacy_std_deviation:{}\n".format(speaker_diplomacy_std_deviation))
            f.write("student_ideology_std_deviation:{}\n".format(student_ideology_std_deviation))
            f.write("speaker_ideology_std_deviation:{}\n".format(speaker_ideology_std_deviation))
            f.write("random_seed:{}\n".format(random_seed))

            f.write("speakers\n")

            for speaker in self.speakers:
                f.write("({},{},{})\n".format(speaker.x, speaker.y, speaker.ideology))

            f.write("begin\n")


    def run_model(self):
        for t in range(5):
            print("At timestep %d" % (t))
            self.step(t)

    # So within each step can have the iteration to check for the interactions and then 
    # another iteration to check for the steps to take
    def step(self, t):
        # The first iteration to account for whatever interactions have occurred, and 
        # the second iteration to update change in location (if such a change can occur) for a given agent.
        # So first, go over speakers, and then look into iterating over students
        for speaker in self.speakers:
            # print("at speaker: %s" % (speaker.uid))
            for student in self.find_students(speaker.x, speaker.y, self.speaker_range):
                speaker.interacts_with(student)

        # Now for the second iteration, update position of the students, follows 
        # a random walk
        for student in self.students:
            # print("at student: %s, current position x: %d, y: %d" % (student.uid, student.x, student.y))
            self.move_student(student)
            # print("still at student: %s, new position x: %d, y: %d" % (student.uid, student.x, student.y))

        self.write_timestep_to_log(t)

    def write_timestep_to_log(self, t):
        student_strings = "".join(map(str, self.students))
        with open(self.log_filename, "a") as f:
            f.write("{}:{}\n".format(t, "".join(student_strings)))
    
    def write_final_log_portion(self):
        with open(self.log_filename, "a") as f:
            f.write("end\n")
        # TODO: add experiment outputs

    # Function to search for unoccupied spaces surrounding given student and randomly select one of the
    # available spaces to move the student to. Currently have hardcoded max distance to move to 2, 
    # might be interesting to make this a parameter to the experiment
    def move_student(self, student):
        max_move_distance = 1
        center_x = student.x
        center_y = student.y
        x_min = max(center_x - max_move_distance, 0)
        y_min = max(center_y - max_move_distance, 0)
        x_max = min(center_x + max_move_distance + 1, GRID_SIZE)
        y_max = min(center_y + max_move_distance + 1, GRID_SIZE)
        found_open_space = set()
        for r in range(x_min, x_max):
            for c in range(y_min, y_max):
                if self.grid[r,c] == None:
                    print("student at ({},{}) can move to ({},{})".format(student.x, student.y, r, c))
                    found_open_space.add((r, c))
        if not len(found_open_space) == 0:
            space_chosen = random.sample(found_open_space, 1)
            student.set_position(space_chosen[0][0], space_chosen[0][1])

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
                    # print("found student %s at r: %d, c: %d" % (self.grid[r,c].uid, r, c))
                    found_students.add(self.grid[r,c])
        # print("students found:", found_students)
        return found_students
