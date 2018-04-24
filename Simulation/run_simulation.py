#!/usr/bin/env python2
from model import Model

students_to_speakers_ratio = 20
speaker_range = 2

expected_student_diplomacy = 50
expected_speaker_diplomacy = 75
expected_abs_student_ideology = 70
expected_abs_speaker_ideology = 30

student_diplomacy_std_deviation = 10
speaker_diplomacy_std_deviation = 10
student_ideology_std_deviation = 10
speaker_ideology_std_deviation = 20

random_seed = 15

experiment_name = "pop_density_test"
for population_density in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
# population_density = 1
    test_model = Model(
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

        random_seed)
    test_model.run_model()


# experiment_name = "speaker_diplomacy_test"
# population_density = 0.5
# # for expected_abs_speaker_ideology in (10, 30, 50, 70, 90):
# # expected_abs_speaker_ideology = 90
# for expected_speaker_diplomacy in (10, 20, 30, 40, 50, 60, 70, 80, 90):
#     test_model = Model(
#         experiment_name,

#         population_density,
#         students_to_speakers_ratio,
#         speaker_range,

#         expected_student_diplomacy,
#         expected_speaker_diplomacy,
#         expected_abs_student_ideology,
#         expected_abs_speaker_ideology,

#         student_diplomacy_std_deviation,
#         speaker_diplomacy_std_deviation,
#         student_ideology_std_deviation,
#         speaker_ideology_std_deviation,
#         random_seed)
#     test_model.run_model()


# experiment_name = "student_ideology_test"
# population_density = 0.5
# expected_abs_speaker_ideology = 80
# for expected_abs_student_ideology in (10, 30, 50, 70, 90):
#     test_model = Model(
#         experiment_name,

#         population_density,
#         students_to_speakers_ratio,
#         speaker_range,

#         expected_student_diplomacy,
#         expected_speaker_diplomacy,
#         expected_abs_student_ideology,
#         expected_abs_speaker_ideology,

#         student_diplomacy_std_deviation,
#         speaker_diplomacy_std_deviation,
#         student_ideology_std_deviation,
#         speaker_ideology_std_deviation,

#         random_seed)
#     test_model.run_model()
