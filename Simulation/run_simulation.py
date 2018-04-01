#!/usr/bin/env python2
from model import Model

students_to_speakers_ratio = 20
speaker_range = 2

expected_student_diplomacy = 50
expected_speaker_diplomacy = 75
expected_abs_student_ideology = 30
expected_abs_speaker_ideology = 80

student_diplomacy_std_deviation = 10
speaker_diplomacy_std_deviation = 10
student_ideology_std_deviation = 10
speaker_ideology_std_deviation = 10

random_seed = 10

experiment_name = "pop_density_test"
for population_density in (0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
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


experiment_name = "speaker_ideology_test"
population_density = 0.3
for expected_abs_speaker_ideology in (30, 40, 50, 60, 70, 80, 90, 95):
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


experiment_name = "student_ideology_test"
population_density = 0.3
expected_abs_speaker_ideology = 80
for expected_abs_student_ideology in (10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 95):
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
