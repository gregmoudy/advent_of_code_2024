# The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, 
# he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany 
# them as they check the places they think he was most likely to visit.

# As each location is checked, they will mark it on their list with a star. 
# They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, 
# you need to help them get fifty stars on their list before Santa takes off on December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; 
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

import glob
import os

# Get all the day_<int>.py files and import them.
DAY_PYTHON_FILES = glob.glob('./day_*.py')
DAY_MODULE_NAMES = [os.path.splitext(os.path.basename(x))[0] for x in DAY_PYTHON_FILES]
for day_module_name in DAY_MODULE_NAMES:
    exec(f'import {day_module_name}')


if __name__ == '__main__':
    # Run each day solver to view the output and timings.
    for day_module_name in DAY_MODULE_NAMES:
        eval(f'{day_module_name}.run()')
