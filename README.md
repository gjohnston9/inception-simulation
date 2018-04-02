### Setting up

- For the simulation, you will need Python 2 and Python's NumPy library.
- For the visualization software, you will need Java 8 with JavaFX. Using the Oracle JDK instead of OpenJDK will make this easier, since JavaFX comes bundled with the Oracle JDK.

### Running the code

- To run our experiments and generate log files, navigate to the `Simulation` directory and run `python run_simulation.py`
- To visualize the results, navigate to the `Visualization` directory and run `./build.sh && java -jar Visualizer.jar`
- If you can't visualize the results, you can look at the bottom of the generated log files (in the `Logs` directory) to see the value of output variables for each experiment.

### Using the visualizer

- The visualizer has two tabs (sample screenshots of each tab are included in Appendix C of our report). After compiling and running the visualizer using the instructions above, you will be shown the first tab. At the top you can switch between the two tabs, and below these two tabs you can choose which log file (from the `Logs` directory) you want to examine.
- The left side displays the initial position of each student and speaker, colored according to their ideologies. People with a low ideology score (close to -100) are closer to red, people with a high ideology score (close to +100) are closer to blue, and people who are ideologically neutral are purple.
- The right side displays change in ideologies over time. Each horizontal line of pixels shows the ideologies of each student and speaker in the simulation at a given timestep.
- In the bottom right of the screen, you can click the Previous or Next buttons to step through the simulation. You can also click and drag your mouse over the right side of the screen to quickly run through the steps of the simulation.
- Click the Analytics tab to see how output variables of the experiment change as input parameters change. After selecting variables for the horizontal and vertical axes, one data point will be shown on the graph for each log file.
