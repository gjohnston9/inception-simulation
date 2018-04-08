import numpy as np
import matplotlib.pyplot as plt

import random

num_samples = 200
ideologies = [30, 80]
std_dev = 8

low_ideologies = np.random.normal(ideologies[0], std_dev, num_samples)
high_ideologies = np.random.normal(ideologies[1], std_dev, num_samples)

low_ideologies = np.clip(low_ideologies, -100, 100) # trim to be between -100 and 100
high_ideologies = np.clip(high_ideologies, -100, 100)

low_ideologies *= np.random.choice([-1,1], size=num_samples) # randomly flip sign
high_ideologies *= np.random.choice([-1,1], size=num_samples)

bins = np.linspace(-100, 100, 40)

fig, ax = plt.subplots()
ax.hist(low_ideologies, bins=bins, color='yellow', alpha=0.5, label='average of absolute value of ideology: {}'.format(ideologies[0]))
ax.hist(high_ideologies, bins=bins, color='blue', alpha=0.5, label='average of absolute value of ideology: {}'.format(ideologies[1]))

ax.set(
	title='frequency of ideology scores',
	xlabel='ideology score',
	ylabel='frequency')
ax.legend()

save_name = '../Report/ideology_scores.png'
print('saving plot to {}'.format(save_name))
plt.savefig(save_name)
