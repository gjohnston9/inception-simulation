from agents import Speaker, Passerby

import random

GRID_SIZE = 100

class Model:
    def __init__(self, num_passersby, num_speakers, speaker_range, ideology_variance, diplomacy_variance):
        # Right now this is a square grid where passersby are placed randomly.
        # If we want to specifically model Skiles walkway, then we can look at using
        # a rectangular grid with speakers placed near the bottom and top.
        self.passerby_grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.speakers = [] # Speakers are stationary and have their own x and y attributes
        self.speaker_range = speaker_range

        for n in range(num_passersby):
            x = random.randrange(GRID_SIZE)
            y = random.randrange(GRID_SIZE)
            passerby = Passerby(ideology_variance, diplomacy_variance)
            self.passerby_grid[x][y].append(passerby)
        
        for n in range(num_speakers):
            x = random.randrange(GRID_SIZE)
            y = random.randrange(GRID_SIZE)
            speaker = Speaker(ideology_variance, diplomacy_variance, x, y)
            self.speakers.append(speaker)

    def run_model(self):
        for t in range(500):
            self.step()

    def step(self):
        # First, model speaker-passerby interactions. Each speaker interacts with
        # all nearby passerby. Speaker_range defines the maximum distance at
        # which a speaker will interact with a passerby.
        for speaker in self.speakers:
            for passerby in self.find_passersby(speaker.x, speaker.y, self.speaker_range):
                speaker.interacts_with(passerby)

        # Next, model all passerby-passerby interactions. Each passerby interacts
        # with a random passerby on the same tile or on an adjacent tile.
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                passersby = self.passerby_grid[x][y] # list of all passersby at this position
                for passerby in passersby:
                    nearby_passersby = self.find_passersby(x, y, 1)
                    if len(nearby_passersby) != 1: # if 1, there are no passersby in range besides this person
                        other_person = random.choice(nearby_passersby)
                        while other_person is passerby: # avoid having someone interact with themselves
                            other_person = random.choice(nearby_passersby)
                        person.interacts_with(other_person)

    def find_passersby(self, center_x, center_y, max_range):
        # Returns a list of all people who are at most max_range units away
        # from position (center_x, center_y)
        x_min = max(center_x - max_range, 0)
        y_min = max(center_y - max_range, 0)
        x_max = min(center_x + max_range + 1, GRID_SIZE)
        y_max = min(center_y + max_range + 1, GRID_SIZE)
        passersby = []
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                passersby.extend(self.passerby_grid[x][y])
        return passersby
